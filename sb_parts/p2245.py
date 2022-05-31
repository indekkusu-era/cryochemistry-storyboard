from random import random, choice

from sb_helper import SBObject, Scale, StoryBoard
from sb_helper import parse_beatmap
from sb_helper import display

FONT = 'WinterKei-eZZRl.ttf'; SIZE = 40; POS = (360, 200); POS_TITLE = (360,240)

artist = "BilliumMoto x Akiri"
title = "Cryochemistry"

"""
TODO Fix the hell out of weird text spacing : AHRDER
"""

def rng_text(text, chance):
    new_text = ""
    for ch in text:
        if random() < chance or ch == " ":
            new_text += ch
        else:
            new_text += ' '
    return new_text

ofs_start_rng = 2238
ofs_end_rng = 11893
period = 7500/174
slope_chance = 1 / (ofs_end_rng - ofs_start_rng)
get_chance = lambda t: (t - ofs_start_rng) * slope_chance

def storyboard_rng():
    overlay_objs = []

    black = SBObject('black.jpg')
    black.add_action(Scale(0, 0, 0, 5, 5))
    black.add_action(Scale(0, 13272, 13272, 0, 0))
    overlay_objs.append(black)
    i = ofs_start_rng
    while i < ofs_end_rng:
        chance = get_chance(i)
        artist_rng = rng_text(artist, chance)
        title_rng = rng_text(title, chance)
        overlay_objs += display(artist_rng, int(i), int(i + period - 1), POS, FONT, SIZE)
        overlay_objs += display(title_rng, int(i), int(i + period - 1), POS_TITLE, FONT, SIZE)
        i += period
    return overlay_objs

def text_gone():
    objs = []
    points = [11893, 12238, 12755, 13100]
    objs += display(artist, points[0], points[2], POS, FONT, SIZE)
    objs += display(title, points[0], points[1], POS_TITLE, FONT, SIZE)
    objs += display("BilliumMoto", points[2], points[3], POS, FONT, SIZE)
    return objs

def p2245():
    return storyboard_rng() + text_gone()