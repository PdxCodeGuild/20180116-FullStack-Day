"""
Lab 16
Finally, some images!
"""

from PIL import Image
import colorsys
import numpy
import imageio


# Pillow uses ints for RGB values, in the range of 0-255
# 'Y' is used to represent the brightness
# To convert to greyscale, set R, G, and B to Y
# Formula for brightness: Y = 0.299*R + 0.587*G + 0.114*B

img = Image.open("images/lenna.png")    # must be in same folder
width, height = img.size                # breaking up the tuple of (512, 512)
pixels = img.load()                     # allocates storage for the image and loads the pixel data

print(img.format, img.size, img.mode)   # shows: PNG (512, 512) RGB
print(type(pixels))
print(pixels)

img.show()

# make greyscale

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        y = 0.299 * r + 0.587 * g + 0.114 * b
        int(y)

        pixels[i, j] = (int(y), int(y), int(y))

img.show()

