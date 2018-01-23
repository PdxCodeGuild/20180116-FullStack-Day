from PIL import Image
import imageio
import colorsys
import numpy


images = []
img = Image.open("./gifs/lenna.png")
np_img = numpy.asarray(img)
print(np_img.shape)

width, height = img.size
pixels = img.load()

images = []

#
for k in range(10):
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]


            r = (r + 13) % 256
            g = (g + 13) % 256
            b = (b + 13) % 256

            pixels[i, j] = (r, g, b)

    np_img = numpy.asarray(img)
    images.append(np_img)

imageio.mimsave('./gifs/lenna.gif', images)
#
#
