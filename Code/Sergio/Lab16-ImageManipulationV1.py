# "Lab 15: Image Manipulator, Version 1"
# from PIL import Image
#
# img = Image.open('Lenna2.png') # must be in same folder
# width, height = img.size
# pixels = img.load()
#
# img = Image.open('Lenna2.png').convert('L')
# img.show()

from PIL import Image
img = Image.open("Lenna2.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        y = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
        r, g, b = y,y,y
        pixels[i,j] = r, g, b
img.show()

