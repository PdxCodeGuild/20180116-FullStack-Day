from PIL import Image
import colorsys
img = Image.open("lenna.png")  # must be in same folder
width, height = img.size
pixels = img.load()
#Y = 0.299*R + 0.587*G + 0.114*B

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        y = 0.299 * r + 0.587 * g + 0.114 * b
        y = int(y)
        # r = 0
        # g = y
        # b = 0

        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

     # do some math on h, s, v
        h = 124
        # s = 100
        # v = 100

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

         # convert back to [0, 255]

        r = int(r*255)
        g = int(g*255)
        b = int(b*255)

        pixels[i, j] = (r, g, b)

img.show()
