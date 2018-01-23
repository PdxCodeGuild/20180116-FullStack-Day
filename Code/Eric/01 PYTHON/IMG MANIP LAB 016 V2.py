# V2: MANIPULATING WITH HSV!! TURNS IT PURPLE!!!

import colorsys
from PIL import Image
img = Image.open("Lenna.png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        Y = 0.299 * r + 0.587 * g + 0.114 * b
        r, g, b = Y, Y, Y
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

        h = float(h)
        h += .7
        s = float(s)
        s += .4
        v = float(v)
        v += .2

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        r = int(r*255)
        g = int(g*255)
        b = int(b*255)

        pixels[i, j] = (r, g, b)

img.show()
