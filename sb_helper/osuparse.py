import os
import json
import numpy as np

class HitObject:
    def __init__(self, code):
        data = code.split(",")
        self.lane = int(data[0])
        self.samplesound = int(data[1])
        try:
            self.offset = int(data[2])
        except:
            self.offset = data[2]
        self.type = int(data[3])
        self.hitsound = int(data[4])
        self.release = -1
        if self.type == 128:
            try:
                self.release = int(data[-1].split(":")[0])
            except:
                self.release = data[-1].split(":")[0]
    
    def get_column_8k(self):
        return max(0, (self.lane - 32) // 64)

    def anti_LN(self):
        self.release = -1
        self.type = 1

    def encode(self):
        a = "0:0:0:0:"
        if self.type == 128:
            a = str(self.release) + ":" + a
        return "{},{},{},{},{},{}".format(self.lane, self.samplesound, self.offset, self.type, self.hitsound, a)
    
    def to_fnf_hitobject(self):
        return [self.offset,self.get_column_8k(),self.release - self.offset if self.type == 128 else 0]

class TimingPoint:
    def __init__(self, code):
        data = code.split(",")
        self.offset = float(data[0])
        self.isBPM = int(data[-2])
        if self.isBPM == 1:
            self.velocity = 60000 / float(data[1])
        else:
            self.velocity = -100 / float(data[1])
        self.timeSignature = int(data[2])
        self.hitsoundvolume = int(data[5])
        self.isKiai = int(data[-1])
    
    def switch(self, mainbpm):
        if self.isBPM == 1:
            self.velocity = self.velocity / mainbpm
            self.isBPM = 0
        else:
            self.velocity = mainbpm * self.velocity
            self.isBPM = 1
    
    def encode(self):
        vel = 60000 / self.velocity if self.isBPM == 1 else -100 / self.velocity
        return "{},{},{},1,0,{},{},{}".format(self.offset, vel, self.timeSignature, self.hitsoundvolume, self.isBPM, self.isKiai)

class osufile:
    def __init__(self, data: str):
        self.data = data.split("\n")
        self.General = None
        self.editor = None
        self.metadata = None
        self.difficulty = None
        self.TimingPoints = list()
        self.HitObjects = list()
        self.initialize_data()
        
    def initialize_data(self):
        self.parseGeneral()
        self.parseEditor()
        self.parseMetadata()
        self.parseDifficulty()
        self.parseTimingPoints()
        self.parseHitObjects()
    
    def parseGroup(self, keyword):
        start = self.data.index("[{}]".format(keyword)) + 1
        end = self.data[start:].index("") + start
        group = dict()
        for data in self.data[start:end]:
            d = data.split(":")
            try:
                group[d[0]] = int(d[1])
            except:
                try:
                    group[d[0]] = float(d[1])
                except:
                    group[d[0]] = d[1]
        return group

    def parseGeneral(self):
        self.General = self.parseGroup("General")
    
    def parseEditor(self):
        self.editor = self.parseGroup("Editor")
        if "Bookmarks" in self.editor.keys():
            self.editor["Bookmarks"] = [int(k) for k in self.editor["Bookmarks"].split(",")]
    
    def parseMetadata(self):
        self.metadata = self.parseGroup("Metadata")
        self.metadata["Tags"] = self.metadata["Tags"].split(" ")
    
    def parseDifficulty(self):
        self.difficulty = self.parseGroup("Difficulty")
    
    def parseTimingPoints(self):
        start = self.data.index("[TimingPoints]") + 1
        end = self.data[start:].index("") + start
        for data in self.data[start:end]:
            self.TimingPoints.append(TimingPoint(data))
    
    def parseHitObjects(self):
        start = self.data.index("[HitObjects]") + 1
        end = self.data[start:].index("") + start
        for data in self.data[start:end]:
            self.HitObjects.append(HitObject(data))
    
    def get_hitobjects(self, start, end):
        return list(filter(lambda x: start <= x.offset < end, self.HitObjects))

    def to_fnf(self):
        isPlayer = True
        # if self.HitObjects[0].get_column_8k() >= 4:
        #     isPlayer = True
        
        Notes = []
        for start, end in zip(self.editor['Bookmarks'][:-1], self.editor['Bookmarks'][1:]):
            section = self.get_hitobjects(start, end)
            sectionNote = {
                "lengthInSteps": 16,
                "mustHitSection": isPlayer,
                "typeOfSection": 0,
                "sectionNotes": [note.to_fnf_hitobject() for note in section]
            }
            # isPlayer = not isPlayer
            Notes.append(sectionNote)
        
        fnf = {"song": {"song": f"{self.metadata['Title']}", "notes": Notes}}
        
        return fnf
    
    def to_taiko(self):
        prevoffset = 0
        prevNotes = []
        def to_taiko_notes(prevNotes):
            if len(prevNotes) == 1:
                if prevNotes in [[0], [3]]:
                    return 8
                if prevNotes in [[1], [2]]:
                    return 0
            if len(prevNotes) == 2:
                if (2 in prevNotes and 1 in prevNotes) or (0 in prevNotes and 1 in prevNotes):
                    return 4
                if (0 in prevNotes and 3 in prevNotes) or (2 in prevNotes and 3 in prevNotes):
                    return 12
            if len(prevNotes) == 3:
                if (2 in prevNotes and 1 in prevNotes):
                    return 4
                if (0 in prevNotes and 3 in prevNotes):
                    return 12
            
            return 12

        taiko_pattern = []
        for hitobject in self.HitObjects:
            hitobject: HitObject
            offset = hitobject.offset
            if offset == prevoffset:
                prevNotes.append(hitobject.lane // 128)
            else:
                if prevoffset:
                    taiko = to_taiko_notes(prevNotes)
                    taiko_pattern.append(f"256,192,{prevoffset},1,{taiko},0:0:0:0:\n")
                prevoffset = offset
                prevNotes = [hitobject.lane // 128]
        return "".join(taiko_pattern)
    
    def anti_ln_spray(self):
        new_hit = []
        for h in self.HitObjects:
            h.anti_LN()
            new_hit.append(h)
        self.HitObjects = new_hit.copy()
    
    def __getitem__(self, rnge: slice):
        t = self
        start = rnge.start
        stop = rnge.stop
        t.HitObjects = list(filter(lambda x: start <= x.offset < stop, t.HitObjects))
        return t
    
    def __repr__(self):
        initializestring = "osu file format v14\n\n"
        initializestring += "[General]\n"
        for key, value in zip(self.General.keys(), self.General.values()):
            initializestring += "{}:{}\n".format(key, value)
        initializestring += "\n"
        initializestring += "[Editor]\n"
        for key, value in zip(self.editor.keys(), self.editor.values()):
            initializestring += "{}:".format(key)
            if key == "Bookmarks":
                initializestring += str(self.editor[key])[1:len(str(self.editor[key])) - 1]
                initializestring += "\n"
                continue
            initializestring += "{}\n".format(value)
        initializestring += "\n"
        initializestring += "[Metadata]\n"
        for key, value in zip(self.metadata.keys(), self.metadata.values()):
            initializestring += "{}:".format(key)
            if key == "Tags":
                initializestring += " ".join(self.metadata[key])
                initializestring += "\n"
                continue
            initializestring += "{}\n".format(value)
        initializestring += "\n[Difficulty]\n"
        for key, value in zip(self.difficulty.keys(), self.difficulty.values()):
            initializestring += "{}:{}\n".format(key, value)
        initializestring += '\n[Events]\n//Background and Video events\n0,0,"blank.jpg",0,0\n//Break Periods\n//Storyboard Layer 0 (Background)\n//Storyboard Layer 1 (Fail)\n//Storyboard Layer 2 (Pass)\n//Storyboard Layer 3 (Foreground)\n//Storyboard Sound Samples\n'
        initializestring += "\n[TimingPoints]\n"
        for tp in self.TimingPoints:
            initializestring += tp.encode() + "\n"
        initializestring += "\n"
        initializestring += "[HitObjects]\n"
        for hit in self.HitObjects:
            initializestring += hit.encode() + "\n"
        initializestring += "\n"
        return initializestring


def parse_beatmap(file):
    # this doesn't work with japanese and unicode metadata
    with open(file, "r") as f:
        data = f.read()
        return osufile(data)


