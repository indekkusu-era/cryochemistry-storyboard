from sb_helper import Fade, SBObject, Scale, StoryBoard
from sb_helper import parse_beatmap
from sb_helper.text_image import get_text_image

def red_effect():
    red_path = 'sb_color/ff0000.png'
    red = SBObject(red_path)
    red.add_actions([
        Scale(0, 346596, 346596, 1.5, 1.5),
        Fade(0, 346596, 346596, 0.125, 0.125),
        Fade(0, 350512, 350512, 0.25, 0.25),
        Fade(0, 353707, 353707, 0.375, 0.375),
        Fade(0, 355485, 355485, 0.4375, 0.4375),
        Fade(0, 357263, 357263, 0.5, 0.5),
        Fade(0, 360819, 360819, 0.625, 0.625),
        Fade(0, 364374, 364374, 0.75, 0.75),
        Fade(0, 367930, 367930, 0.875, 0.875),
        Fade(0, 371485, 371485, 1, 1),
        Fade(0, 375263, 387263, 1, 0)
    ])
    return [red]

def end():
    black = SBObject('black.jpg')
    # 388096
    ending_text = "Symperasma Boreatica"
    get_text_image(ending_text, 'sb_misc/ending.png', 'WinterKei-eZZRl.ttf', 40)
    black.add_actions([
        Scale(0, 385707, 385707, 5, 5),
        Fade(0, 385707, 388096, 0, 1)
    ])
    ending = SBObject('sb_misc/ending.png')
    ending.add_actions([
        Fade(0, 385707, 385930, 0, 1),
        Scale(0, 385763, 387485, 1, 0.95),
        Scale(0, 388041, 388078, 0.95, 0)
    ])
    return [black, ending]

def p360819():
    return red_effect() + end()