from PIL import Image

import colorsys

# Version 1
img = Image.open("Lenna_image.png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r,g,b = pixels[i, j]

        r,g,b = (int(0.299 * float(r)), int(0.587 * float(g)),int(0.114 * float(b)))
        pixels[i, j] = (r, g, b)


img.show()

