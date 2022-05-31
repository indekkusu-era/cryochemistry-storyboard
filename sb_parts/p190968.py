from sb_helper.text_image import randomglitcheffect
from sb_helper import Fade, SBObject, Scale
from sb_helper import parse_beatmap

def random_glitch(start, end, freq):
    sbobjs = []
    proba_slope = 1.5 / (end - start)
    proba = lambda t: min((t - start) * proba_slope, 1)
    i = start
    while i < end:
        ofs = int(i)
        obj = f'sb_misc/{ofs}.png'
        randomglitcheffect(obj, 200, 200, (0,0,0), proba(i))
        sbobj = SBObject(obj)
        sbobj.add_actions([
            Scale(0, ofs, ofs, 5, 5),
            Scale(0, ofs + int(freq), ofs + int(freq), 0, 0)
        ])
        sbobjs.append(sbobj)
        i += freq
    return sbobjs

def p190968():
    objs = []
    crack = SBObject('crack.png')
    crack.add_actions([
        Scale(0, 200566, 200566, 1.5, 1.5),
        Scale(0, 237137, 237137, 0, 0)
    ])
    black = SBObject('black.jpg')
    black.add_actions([
        Scale(0,235994, 235994, 5, 5),
        Scale(0, 237137, 237137, 0, 0)
    ])
    return objs + [crack, black]

def p190958_overlay():
    objs = []
    objs += random_glitch(199396, 200566, 15000/205)
    return objs