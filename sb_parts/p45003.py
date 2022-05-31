from sb_helper import Fade, SBObject, Scale, StoryBoard
from sb_helper import parse_beatmap
from .snowstorm import snowstorm

points = parse_beatmap('fast_snowstorm.osu').HitObjects
points = [i.offset - 7 for i in points]

def faster_snowstorm(offset):
    return snowstorm(offset, offset + 1, 5, 100, True)

def p45003_overlay():
    black_grad = SBObject('sb_color/000000.png')
    black = SBObject('black.jpg')
    black_grad.add_actions([
        Scale(0, 44651, 44651, 1.5, 1.5),
        Fade(0, 44651, 44996, 0, 1),
        Fade(1, 44996, 46375, 1, 0.5),
        Fade(0, 90513, 90513, 0, 0)
    ])
    black.add_actions([
        Scale(0, 44996, 46375, 5, 5),
        Fade(1, 44996, 46375, 1, 0)
    ])
    fast_storm = []
    for p in points:
        fast_storm += faster_snowstorm(p)
    return [black_grad, black] + fast_storm


def p45003():
    return []