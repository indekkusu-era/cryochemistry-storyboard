from sb_helper import StoryBoard
from sb_helper.sb_base import Fade, SBObject, Scale
from sb_parts import p2245, p154519, p90520, p190968, p190958_overlay, penguin_suggestions, snowstorm, p45003_overlay, p45003, reverse_snowstorm, p126068, p154512_snowstorm, p273708, p360819, mapper_sb, intro
from sb_parts.p303930 import p303930
from sb_parts.effects import effect1, effect2, effect3

osb_fp = "BilliumMoto x Akiri - Cryochemistry (DannyPX).osb"

def BONK():
    black = SBObject('black.jpg')
    black.add_actions([
        Scale(0, 388096, 388096, 5, 5),
        Scale(0, 400000, 400000, 0, 0)
    ])
    return black

def main():
    effects = effect1() + effect2(10) + effect3()
    background = effects + p2245() + p90520() + p190968() + p154519() + p45003() \
         + p360819() + p126068() + p154512_snowstorm() + p273708() \
             + p303930() + p190958_overlay() + p45003_overlay() + penguin_suggestions() + snowstorm(0, 11893, 1, 222) + snowstorm(44996, 102846, 1, 222) \
                 + reverse_snowstorm(318152, 353819, 1.5, 222)
    foreground = mapper_sb() + intro()
    overlay = [BONK()]
    sb = StoryBoard(background_objects=background, overlay_objects=overlay, foreground_objects=foreground)
    sb.osb(osb_fp)

if __name__ == "__main__":
    main()