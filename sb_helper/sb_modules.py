import os
from typing import List
from .sb_base import Move, Fade, SBObject
from .text_image import generate_characters

def generate_char_sb_object(characters, font, size, folder='sb_char'):
    # generate_characters(characters, font, size, folder)
    f_str = folder + "/{}.png"
    ascii_ = [str(ord(chrs)) for chrs in characters]
    sb_char_dict = {}
    for char_code in ascii_:
        if not(f'{char_code}.png' in os.listdir(folder)):
            generate_characters(chr(int(char_code)), font, size, folder)
        sb_char_dict[char_code] = SBObject(f_str.format(char_code))
    return sb_char_dict

def display(string: str, start:int, end:int, pos: tuple, font_file, size):
    sb_chars = []
    x, y = pos
    L = 0
    len_chars = len(''.join(string))
    for i, char in enumerate(string):
        sbobj = generate_char_sb_object(char, font_file, size)
        asc = str(ord(char))
        pos_char_x = int(x + (L - (len_chars + 1) / 2) * size)
        sbobj[asc].add_action(Move(1, start, end, (pos_char_x, y), (pos_char_x, y)))
        sbobj[asc].add_action(Fade(0, start, start + 1, 0, 1))
        sbobj[asc].add_action(Fade(0, end, end + 1, 1, 0))
        sb_chars.append(sbobj[asc])
        L += 1
    
    return sb_chars.copy()
