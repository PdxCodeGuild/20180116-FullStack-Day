from PIL import Image
import colorsys
import math



# Use colorsys to adjust image by HSV
img = Image.open("./gifs/lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()


for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        # Arbitrarily change HSV values
        h = .2 * h
        s = .9 * s
        v = .6 * v

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        # convert back to [0, 255]

        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)

        pixels[i, j] = (r, g, b)

img.show()