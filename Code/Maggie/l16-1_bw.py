# Image manipulation

# Convert an image to greyscale using the Pillow Library
from PIL import Image

# from https://github.com/PdxCodeGuild/20180116-FullStack-Day/blob/master/1%20Python/labs/lab16-image_manipulation.md
img = Image.open("lenna.png") # will open image; must be in same folder
width, height = img.size
pixels = img.load()
img_2 = Image.open("lenna.png") #vers 2 for saturation.


for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        Y = round(0.299 * float(r) + 0.587 * float(g) + 0.114 * float(b))  # Y = 0.299*R + 0.587*G + 0.114*B = brightness
        pixels[i, j] = (Y, Y, Y) # (r, g, b) #every single pixel has an rgb value

img.show()  # show image converted to b & w

