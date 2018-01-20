from PIL import Image

img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        y = 0.299 * r + 0.587 * g + 0.114 * b
        int(y)

        pixels[i, j] = (int(y), int(y), int(y))

img.show()



'''
'Y' is used to represent the brightness.
 The following formula get the brightness of an 
 RGB triplet. To convert to greyscale, set R, G, and B to Y.
 '''