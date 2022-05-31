from sb_helper import Fade, SBObject, Scale, StoryBoard
from sb_helper import parse_beatmap

from sb_helper.text_image import gradient, randomglitcheffect

def transition():
    black = SBObject('black.jpg')
    black.add_actions(
        [
            Scale(0, 97179, 97179, 5, 5),
            Scale(0, 97624, 97624, 0, 0),
            Scale(0, 122512, 122512, 5, 5),
            Scale(0,126068, 126068, 0, 0)
        ]
    )

    gradient((0,0,0), 'sb_color/000000.png')
    black_grad = SBObject('sb_color/000000.png')
    black_grad.add_actions(
        [
            Scale(0, 97624, 97624, 1.5, 1.5),
            Fade(0, 152735, 154512, 1, 0)
        ]
    )

    blue_grad = SBObject('sb_color/0000ff.png')
    blue_grad.add_actions(
        [
            Scale(0, 126075, 126075, 1.5, 1.5),
            Fade(0, 152742, 154519, 0, 1)
        ]
    )
    return [black, black_grad, blue_grad]

def transition_0(start, end, freq):
    sbobjs = []
    proba_slope = 1 / (end - start)
    proba = lambda t: (t - start) * proba_slope
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

def p90520():
    black = SBObject('black.jpg')
    black.add_actions([
        Scale(0, 154068, 154068, 5, 5),
        Scale(0, 154512, 154512, 0, 0)
    ])

    return transition_0(90513, 97179, 43) + transition() + [black]