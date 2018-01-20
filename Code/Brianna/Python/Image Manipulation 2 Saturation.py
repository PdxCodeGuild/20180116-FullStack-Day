from PIL import Image
import colorsys

img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        #defining all those pixels
        r, g, b = pixels[i, j]
        y = 0.299 * r + 0.587 * g + 0.114 * b
        int(y)
        # redefining all those pixels by switching stuff about and replacing it with y.
        pixels[i, j] = (int(y), int(y), int(y))

img.show()
# This math does not work when applied below. :-)
for i in range(width):
    for j in range(height):
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        saturated = 0.7 * h + 0.4 * s + 0.3 * v
        int(saturated)
        r, g, b = colorsys.hsv_to_rgb(saturated/255, saturated/255, saturated/255)

img.show()

# colorsys uses colors in the range [0, 1]


# do some math on h, s, v
saturated =

r, g, b = colorsys.hsv_to_rgb(h, s, v)

# convert back to [0, 255]

r = int(r*255)
g = int(g*255)
b = int(b*255)