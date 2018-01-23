"Lab 15: Image Manipulator, Version 1"
from PIL import Image

img = Image.open('Lenna.png') # must be in same folder
width, height = img.size
pixels = img.load()


img = Image.open('Lenna.png').convert('L')
img.show()


