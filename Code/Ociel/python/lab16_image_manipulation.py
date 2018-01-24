from PIL import Image

import colorsys

#######################################################################################
# Version 1
img = Image.open("Lenna_image.png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        y = int(0.299*r + 0.587*g + 0.114*b)
        r, g, b = y, y, y

        #r, g, b = (int(0.299 * float(r)), int(0.587 * float(g)), int(0.114 * float(b)))
        pixels[i, j] = (r, g, b)
#img.show()
#######################################################################################
# Version 2
img_saturation = Image.open("Lenna_image.png")
width_sat, height_sat = img_saturation.size
pixels_sat = img_saturation.load()

# colorsys uses colors in the range [0, 1]
# rgb_to_hsv is a method of colorsys and it coverts coordinates
# it converts the rgb coordinates to hsv coordinates

# do some math on h, s, v
for i in range(width_sat):
    for j in range(height_sat):
        r,g,b = pixels_sat[i,j]
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

        h = h * 0.88
        s = s * 0.88
        v = v * 0.98


        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        # convert back to [0, 255]

        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)

        pixels_sat[i, j] = (int(r),int(b), int(b))

# img_saturation.show()



#######################################################################################
# Version 3
