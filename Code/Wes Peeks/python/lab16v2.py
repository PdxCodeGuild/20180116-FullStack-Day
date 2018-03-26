import colorsys

from PIL import Image
img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        y = int(0.25 * r + 0.25 * g + 0.25 * b)

        # colorsys uses colors in the range [0, 1]
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

        h = float(h)
        h += .10
        s = float(s)
        s += 0.10
        v = float(v)
        v += 0.10
        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        # convert back to [0, 255]

        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)

        # your code here

        pixels[i, j] = (r, g, b)

img.show()