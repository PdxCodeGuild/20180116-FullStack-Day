# Image manipulation

# Alter hue and saturation in colorsys before rendering from PIL import Image
from PIL import Image
import colorsys
from random import random
from math import log
rnd = random()
# from https://github.com/PdxCodeGuild/20180116-FullStack-Day/blob/master/1%20Python/labs/lab16-image_manipulation.md
img = Image.open("lenna.png") # will open image; must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        # colorsys uses colors in the range [0, 1]
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        h, s, v = h*rnd, s*rnd, v*rnd # do some math on h, s, v
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)

        pixels[i, j] = (int(r), int(g), int(b)) #every single pixel has an rgb value

img.show()  # show image with altered values

