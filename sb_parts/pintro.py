from sb_helper.sb_base import Fade, Move, Scale
from sb_helper.text_image import get_text_image
from sb_helper import SBObject

text = [
    ["4 Digit", " MWC 4", " Grand Finals"],
    ["Custom", " Tiebreaker", " Song"],
    ["Storyboard", " By", " HowToPlayLN"],
    ["Collaboration with", " 5", " Mappers"]
]

offset = [
    [13272, 13789, 14306],
    [16031, 16548, 17065],
    [18789, 19306, 19824],
    [21548, 22065, 22582]
]

pos = [(285, 150), (285, 210), (285, 270), (285, 330)]

offset_end = 22927

def display_text_cumulative(list_text, offset, pos, offset_end):
    cur_text = ""
    objs = []
    list_offset = offset + [offset_end]
    for text, ofs, ofs2 in zip(list_text, list_offset[:-1], list_offset[1:]):
        cur_text += text
        fp = f"sb_misc/{ofs}.png"
        get_text_image(cur_text, fp, "WinterKei-eZZRl.ttf", 40)
        text_sb = SBObject(fp)
        text_sb.add_actions([
            Scale(0, ofs, ofs, 1, 1),
            Move(0, ofs, ofs, pos, pos),
            Scale(0, ofs2, ofs2, 0, 0)
        ])
        objs.append(text_sb)

    return objs

def text_emphasizer():
    ofs_start = 13272; ofs_end = 24306
    black = SBObject('black.jpg')
    black.add_actions([
        Scale(0, ofs_start, ofs_start, 5, 5),
        Fade(0, ofs_start, ofs_start, 0.5, 0.5),
        Scale(0, ofs_end, ofs_end, 0, 0)
    ])
    return black

def intro():
    objs = []
    for tex, ofs, pos_ in zip(text, offset, pos):
        objs += display_text_cumulative(tex, ofs, pos_, offset_end)
    return [text_emphasizer()] + objs