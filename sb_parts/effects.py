from random import random, choice
from math import pi
from sb_helper import Fade, SBObject, Scale, Rotate, Move
from sb_helper import parse_beatmap

def big_pulse(offset):
    bg = SBObject('bg.jpg')
    bg.add_actions([
        Fade(0, offset, offset + 200, 0.5, 0),
        Scale(11, offset, offset + 200, 0.35, 0.45)
    ])
    return bg

def small_pulse(offset):
    bg = SBObject('sb_color/000000.png')
    bg.add_actions([
        Fade(0, offset, offset + 200, 0.3, 0),
        Scale(11, offset, offset + 200, 1.5, 1.5)
    ])
    return bg

def bounce():
    objects = parse_beatmap('BilliumMoto x Akiri - Cryochemistry (DannyPX) [big_pulse].osu').HitObjects
    offset = [i.offset for i in objects]
    
    return [big_pulse(i) for i in offset]

def randomsnow(offset, offset_end):
    snow = SBObject('sb_misc/sq.jpg')
    x, y = random() * 840 - 120, random() * 480
    snow.add_actions([
        Scale(1, offset, offset+200, 0, random() * 10),
        Rotate(1, offset, offset + 200, 0, pi/2),
        Move(0, offset, offset, (x,y), (x,y)),
        Scale(0, offset_end, offset_end, 0, 0)
        # Move(0, offset_end-50, offset_end+50, (x,y), (x,480))
    ])
    return snow

def small_bounce():
    objects = parse_beatmap('BilliumMoto x Akiri - Cryochemistry (DannyPX) [small_pulse].osu').HitObjects
    offset = [i.offset for i in objects]
    
    return [small_pulse(i) for i in offset]

def get_snow_batch():
    voice_fp = "BilliumMoto x Akiri - Cryochemistry (DannyPX) [random_snow].osu"
    hitobject_data = parse_beatmap(voice_fp).HitObjects
    """
    Algorithm outline
    Find 1, store it in the batch until find the 2, append 1 in 2d array 1
    Find 2, store it in the batch until find 1, append 2 in 2d array 2
    """
    array_1 = []
    array_2 = []
    array_keep = []
    last_col = 64
    for hitobject in hitobject_data:
        offset = hitobject.offset
        column = hitobject.lane
        if column != last_col:
            if last_col == 64:
                array_1.append(array_keep.copy())
            else:
                array_2.append(array_keep.copy())
            array_keep.clear()
            last_col = column
        array_keep.append(offset)
    if last_col == 64:
        array_1.append(array_keep.copy())
    else:
        array_2.append(array_keep.copy())
    return array_1, array_2

def generate_snow(particle_per_offset=20):
    generates, drops = get_snow_batch()
    assert len(generates) == len(drops)
    objs = []
    for i in range(len(generates)):
        batch_generate = generates[i]
        batch_drops = drops[i]
        for offset in batch_generate:
            for _ in range(particle_per_offset):
                snow = randomsnow(offset, choice(batch_drops))
                objs.append(snow)
    return objs

effect1 = bounce
effect2 = generate_snow
effect3 = small_bounce