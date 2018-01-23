""""
Let's convert an image into greyscale using the Pillow library, which is a fork of PIL 'python image library'.
"""

from PIL import Image

img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        Y = int(0.299 * r + 0.587 * b + 0.114 * b) #convert to int


        pixels[i, j] = (Y, Y, Y) #only print Y

img.show()