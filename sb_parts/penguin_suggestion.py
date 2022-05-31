from sb_helper import Fade, SBObject, Scale, StoryBoard
from .snowstorm import snowstorm, reverse_snowstorm

def cut_to_black(points, ending):
    opacity_freq = 1 / len(points)
    scalar = 5
    black = SBObject('black.jpg')
    black.add_action(Scale(0, points[0], points[0], scalar, scalar))
    cur_freq = opacity_freq
    for p in points:
        black.add_action(Fade(0, p, p, cur_freq, cur_freq))
        cur_freq += opacity_freq
    black.add_action(Fade(0, ending, ending, 0, 0))
    return black

def bg_slowly_fades_in(start, end, freq):
    times = int((end - start) / freq) + 1
    slope = 1 / times
    black = SBObject('black.jpg')
    opa = 1 - slope
    i = start
    black.add_action(Scale(0, start, start, 5, 5))
    for t in range(times):
        black.add_action(Fade(1, int(i), int(i + freq / 2), opa, 1))
        i += freq
        opa -= slope
    black.add_action(Fade(0, int(end - freq / 2), end, 1, 0))
    return black

def penguin_suggestions():
    additional_effects = []
    additional_effects += snowstorm(24306, 34617, 1, 150)
    additional_effects.append(bg_slowly_fades_in(97624, 107846, 60000/135))
    additional_effects.append(cut_to_black([137179, 137846, 138512, 138957, 139624], 140290))
    additional_effects += snowstorm(246280, 246423, 1, 250)
    additional_effects.append(cut_to_black([262566, 262994, 263423, 263708, 264137], 264566))
    black = SBObject('black.jpg')
    # 04:35:485 - 04:49:708
    black.add_actions([
        Scale(0, 275485, 275485, 5, 5),
        Fade(2, 275485, 289708, 1, 0)
    ])
    additional_effects.append(black)
    additional_effects += reverse_snowstorm(350152, 359930, 2.5, 222)
    additional_effects += reverse_snowstorm(353707, 359930, 3.5, 222)
    return additional_effects