from PIL import Image
import colorsys
import os
import imageio
import random

img = Image.open("photo.png") # must be in same folder
width, height = img.size
pixels = img.load()        # do some math on h, s, v

mix = 0
while mix < 11:
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

                    # colorsys uses colors in the range [0, 1]
            h = random.randrange(0.0, 1.0)
            s = random.randrange(0.0, 1.0)
            v = random.randrange(0.0, 1.0)

            r, g, b = colorsys.hsv_to_rgb(h, s, v)

            r = int(r * 255)
            g = int(g * 255)
            b = int(b * 255)

            pixels[i, j] = r, g, b

    img.save("photo" + str(mix) + ".png")
    mix = mix + 1

png_dir = ""
images = []
for subdir, dirs, files in os.walk(png_dir):
    for file in files:
        file_path = os.path.join(subdir, file)
        if file_path.endswith(".png"):
            images.append(imageio.imread(file_path))
imageio.mimsave('.movie.gif', images)




