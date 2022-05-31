from sb_helper.sb_base import Move, Scale
from sb_helper.text_image import get_text_image
from sb_helper import SBObject

POS = (541, 445)

def mapper_sb():

    mappers = {
        'DannyPX': [126068,200566,275485],
        'Penguinosity': [2238,255423],
        'Orca': [90513, 154512],
        'Logan': [180255,237137,360819],
        'HowToPlayLN': [46375,375263]
    }

    all_parts = []

    def generate_file_name(mapper_name):
        return "mapper_name/" + mapper_name + ".png"

    for v in mappers.values():
        all_parts += v
    all_parts = sorted(all_parts) + [388715]

    for k in mappers.keys():
        get_text_image(k, generate_file_name(k), "WinterKei-eZZRl.ttf", 20)

    objects = []
    for start, end in zip(all_parts[:-1], all_parts[1:]):
        mapper_name = ""
        for mapper, sections in mappers.items():
            if start in sections:
                mapper_name = mapper
                break
        a = SBObject(generate_file_name(mapper_name))
        a.add_actions([
            Scale(0, start, start, 1, 1),
            Move(0, start, start, POS, POS),
            Scale(0, end, end, 0, 0)
        ])
        objects.append(a)
    return objects