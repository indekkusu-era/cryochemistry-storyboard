import numpy as np
import os
from PIL import Image, ImageDraw, ImageFont
import textwrap


def get_text_image(text, file_name, font_file, size):
    para = textwrap.wrap(text, width=40)

    MAX_W, MAX_H = 1280,720
    im = Image.open('blank.png')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(
        font_file, size)

    current_h, pad = MAX_H/2 - len(para) * 25, 10
    for line in para:
        w, h = draw.textsize(line, font=font)
        draw.text(((MAX_W - w) / 2, current_h), line, font=font)
        current_h += h + pad

    im.save(file_name)

def generate_characters(characters, font_file, size, folder='sb_char'):
    if folder not in os.listdir():
        os.mkdir(folder)
    
    f_str = folder + "/{}.png"
    for chrs in characters:
        f_name = str(ord(chrs))
        get_text_image(chrs, f_str.format(f_name), font_file, size)

def get_color(RGB: tuple, fp: str):
    color = Image.new('RGB', (1280, 720), RGB)
    color.save(fp)

def gradient(RGB, fp):
    # Define width and height of image
    W, H = 720, 720

    # Create solid red image
    im = Image.new(mode='RGB', size=(W,H), color=RGB)

    # Create radial alpha/transparency layer. 255 in centre, 0 at edge
    Y = np.linspace(-1, 1, H)[None, :]*255
    X = np.linspace(-1, 1, W)[:, None]*255
    alpha = (X**2 + Y**2) ** 0.5
    alpha = np.clip(0,255,alpha)

    # Push that radial gradient transparency onto red image and save
    im.putalpha(Image.fromarray(alpha.astype(np.uint8)))
    im.save(fp)

def rectangle(fp, width, height):
    im = Image.new(mode='RGB', size=(width, height), color=(255,255,255))

    im.save(fp)

def randomglitcheffect(fp, width, height, RGB, chance):
    im = Image.new(mode='RGB', size=(width, height), color=RGB)
    alp = np.random.choice([0,1], p=[1 - chance, chance], size=(width, height)) * 255

    im.putalpha(Image.fromarray(alp.astype(np.uint8)))
    im.save(fp)

def white_ball(fp):
    W, H = 500, 500
    im = Image.new(mode='RGB', size=(W,H), color=(255,255,255))
    
    Y = np.linspace(-1, 1, H)[None, :]*255
    X = np.linspace(-1, 1, W)[:, None]*255
    al = (X ** 2 + Y ** 2) ** 0.5
    al[al<=255] = 255
    al[al > 255] = 0
    
    
    im.putalpha(Image.fromarray(al.astype(np.uint8)))
    im.save(fp)