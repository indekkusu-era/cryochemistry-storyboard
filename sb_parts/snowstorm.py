from math import sin, cos
from random import random
from sb_helper import SBObject
from sb_helper.sb_base import Loop, Fade, Move, Rotate, VectorScale
from sb_helper.text_image import white_ball


fp = 'sb_misc/sq.jpg'

theta = 3.14 / 8

def get_one_unit_vector(theta):
    return sin(theta), cos(theta)

def snow(start, duration, pos_x, pos_y, size):
    x_vec, y_vec = get_one_unit_vector(theta)
    in_loop_actions = [
        Fade(1, 0, 50, 0, 1),
        Move(1, 0, duration, (pos_x, pos_y), (pos_x + x_vec * 1500, pos_y + y_vec * 1500)),
        Fade(1, duration - 50, duration, 1, 0)
    ]
    out_loop_actions = [
        Rotate(0,start,start,theta, theta),
        VectorScale(0,start, start, (size, size), (size, size))
    ]
    return in_loop_actions, out_loop_actions

def wons(start, duration, pos_x, pos_y, size):
    x_vec, y_vec = get_one_unit_vector(theta)
    y_vec *= -1
    in_loop_actions = [
        Fade(1, 0, 50, 0, 1),
        Move(1, 0, duration, (pos_x, pos_y), (pos_x + x_vec * 1500, pos_y + y_vec * 1500)),
        Fade(1, duration - 50, duration, 1, 0)
    ]
    out_loop_actions = [
        Rotate(0,start,start,theta, theta),
        VectorScale(0,start, start, (size, size), (size, size))
    ]
    return in_loop_actions, out_loop_actions

def snowstorm(start: int, end: int, speed: float, n_particles: int, stack=False):
    X_min, Y_min = -640, -480; X_max, Y_max = 640, 0
    dur_min, dur_max = 3500 / speed, 9000 / speed
    delay_min, delay_max = 0, 9000 / speed if not stack else 0
    size_min, size_max = 1, 10
    num_snow = n_particles
    snows = []
    for i in range(num_snow):
        x = int(random() * (X_max - X_min) + X_min)
        y = int(random() * (Y_max - Y_min) + Y_min)
        d = int(random() * (dur_max - dur_min) + dur_min)
        delay = int(random() * (delay_max - delay_min) + delay_min)
        s = random() * (size_max - size_min) + size_min
        snow_i = SBObject(fp)
        snow_loop_times = int((end - start) // d) + 1
        snow_loop_actions, snow_out_loop_actions = snow(start, d, x, y, s)
        snow_loop = Loop(start + delay, snow_loop_times, snow_loop_actions)
        snow_i.add_actions([snow_loop] + snow_out_loop_actions)
        snows.append(snow_i)
    return snows

def reverse_snowstorm(start: int, end: int, speed: float, n_particles: int, stack=False):
    X_min, Y_min = -640, 960; X_max, Y_max = 640, 480
    dur_min, dur_max = 3500 / speed, 9000 / speed
    delay_min, delay_max = 0, 9000 / speed if not stack else 0
    size_min, size_max = 1, 10
    num_snow = n_particles
    snows = []
    for i in range(num_snow):
        x = int(random() * (X_max - X_min) + X_min)
        y = int(random() * (Y_max - Y_min) + Y_min)
        d = int(random() * (dur_max - dur_min) + dur_min)
        delay = int(random() * (delay_max - delay_min) + delay_min)
        s = random() * (size_max - size_min) + size_min
        snow_i = SBObject(fp)
        snow_loop_times = int((end - start) // d) + 1
        snow_loop_actions, snow_out_loop_actions = wons(start, d, x, y, s)
        snow_loop = Loop(start + delay, snow_loop_times, snow_loop_actions)
        snow_i.add_actions([snow_loop] + snow_out_loop_actions)
        snows.append(snow_i)
    return snows