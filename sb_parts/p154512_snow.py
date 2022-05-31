from sb_helper import SBObject
from .snowstorm import snowstorm


def p154512_snowstorm():
    objs = []
    speed = [1.5,2.5,3.5,4.5]
    offset = [154512, 161624, 168244, 174437, 180255]
    for i in range(len(speed)):
        end = 9000 / speed[i]
        objs += snowstorm(offset[i], offset[i + 1] - end, speed[i], 400)

    return objs