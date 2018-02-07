import colorsys
from PIL import Image
img = Image.open("Lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

#
# for i in range(width):
#     for j in range(height):
#         r, g, b = pixels[i, j]
#         Y = 0.299 * r + 0.587 * g + 0.114 * b
#         r = int(Y)
#         g = int(Y)
#         b = int(Y)
#         pixels[i, j] = (r, g, b)
#
# pixels[i, j] = (r, g, b)
#
# img.show()


####Version 2 #################
# for i in range(width):
#     for j in range(height):
#         r, g, b = pixels[i, j]
#         h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
#         # Arbitrarily change HSV values
#         h = .2 * h
#         s = .9 * s
#         v = .6 * v
#
#         r, g, b = colorsys.hsv_to_rgb(h, s, v)
#
#         # convert back to [0, 255]
#
#         r = int(r * 255)
#         g = int(g * 255)
#         b = int(b * 255)
#
#         pixels[i, j] = (r, g, b)
#
# img.show()

############VERSION 3#####################
from PIL import Image, ImageDraw


width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)

####### HEAD ##########
draw.ellipse((200, 50, 300, 150), outline = "red", fill='green')

#######TORSO ##########
draw.line((250, 150, 250, 350), width = 2, fill = "blue")

###### ARMS ###########
draw.line((250, 200, 300, 150), width = 2, fill = "blue")
draw.line((250, 200, 200, 150), width = 2, fill = "blue")

####### LEGS ###########
draw.line((250, 350, 350, 450), width = 2, fill = "blue")
draw.line((250, 350, 150, 450), width = 2, fill = "blue")

img.show()





