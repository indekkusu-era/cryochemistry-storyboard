from random import random, choice

from sb_helper import Fade, SBObject, Scale, StoryBoard
from sb_helper import parse_beatmap
from sb_helper import display

from sb_helper.text_image import gradient

FONT = 'WinterKei-eZZRl.ttf'; SIZE = 40; POS = (360, 200); POS_TITLE = (360,240)

rgb_start = (0,0,255); rgb_mid = (255, 0, 255); rgb_end = (255, 0, 0)

def get_color_scale(t, s, m, e):
    if t < 0.5:
        start = s; end = m
    else:
        start = m; end = e; t -= 0.5
    
    slope = tuple([(en - st) * 2 for en, st in zip(end, start)])

    return tuple([int(st + t * sl) for st, sl in zip(start, slope)])

def get_color_code_str(rgb):
    return '%02x%02x%02x' % rgb

def color_appear(start: int, end: int, rgb, transparency):
    fp = "sb_color/" + get_color_code_str(rgb) + ".png"
    gradient(rgb, fp)
    cl = SBObject(fp)
    cl.add_action(Scale(0, start, start, 1.5, 1.5))
    cl.add_action(Fade(0, start, end - 1, transparency, transparency))
    cl.add_action(Fade(0, end-1, end, transparency, 0))
    return cl

def scaling_sb(points, start, mid, end, transparency):
    sb_objs = []
    get_t = lambda p: (p - points[0]) / (points[-2] - points[0])
    for p, p2 in zip(points[:-1], points[1:]):
        t = get_t(p)
        color = get_color_scale(t, start, mid, end)
        cl_sb = color_appear(int(p), int(p2), color, transparency)
        sb_objs.append(cl_sb)
    return sb_objs

points = [154519, 161631, 168251, 174444, 180262, 185779, 190968, 195891, 200573, 237144]
points = [p - 7 for p in points]

def p154519():
    return scaling_sb(points, rgb_start, rgb_mid, rgb_end, 0.75)