from PIL import Image
import colorsys

img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()


# This math does not work when applied below. :-)
for i in range(width):
    for j in range(height):
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

        h = h * .7
        s = s * .7
        v = v * .7

pixels[i, j] = (r, g, b)

img.show()

# colorsys uses colors in the range [0, 1]


# convert back to [0, 255]

r = int(r*255)
g = int(g*255)
b = int(b*255)