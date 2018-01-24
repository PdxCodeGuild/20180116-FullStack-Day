"""
Use the colorsys library to increase the saturation, decrease the saturation, and rotate the hue. Colorsys represents
colors as floats in the range 0.0 - 1.0, whereas pillow uses ints in the range 0 - 255. You'll have to convert between
these two representations.
"""

import colorsys
from PIL import Image

img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        # colorsys uses colors in the range [0, 1]
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

        # do some math on h, s, v --> multiply by 2
        h *= 2
        s *= 2
        v *= 2

        #convert back to r, g, b
        r, g, b = colorsys.hsv_to_rgb(h, s, v)


        # convert back to [0, 255]
        r = int(r*255)
        g = int(g*255)
        b = int(b*255)

        pixels[i, j] = r, g, b


img.show()