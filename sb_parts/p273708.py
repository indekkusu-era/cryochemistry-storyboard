from sb_helper import SBObject
from sb_helper.sb_base import Scale
from .p190968 import random_glitch

def p273708():
    black = SBObject('black.jpg')
    h = random_glitch(273708, 274596, 56)
    black.add_actions([
        Scale(0, 274596, 274596, 5, 5),
        Scale(0, 275485, 275485, 0, 0)
    ])
    return h + [black]