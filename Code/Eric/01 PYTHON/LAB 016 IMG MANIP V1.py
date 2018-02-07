# V1 CONVERT IMAGE TO GREYSKULL!

from PIL import Image
img = Image.open("Lenna.png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        Y = int(0.299*r + 0.587*g + 0.114*b)
        r, g, b = Y, Y, Y
        pixels[i, j] = (r, g, b)

img.show()
