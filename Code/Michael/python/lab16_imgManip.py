# Let's convert an image into greyscale using the Pillow library, which is a fork of PIL 'python image library'. First download the file and place it in the same directory as your code (or save it anywhere and use an absolute path when opening it). If you don't have pillow installed, run pip install pillow in a terminal. You can check if pillow using pip show pillow.
#
# Use the formula for converting to greyscale and the code below. Remember that Pillow uses ints for RGB values, in the range of 0-255, whereas your math will often use floats. 'Y' is used to represent the brightness. The following formula get the brightness of an RGB triplet. To convert to greyscale, set R, G, and B to Y.
#

# from PIL import Image
# img = Image.open("lenna.png") # must be in same folder
# width, height = img.size
# pixels = img.load()
# complex
# for i in range(width):
#     for j in range(height):
#         r, g, b = pixels[i, j]
#
#         y = int(0.299 * r + 0.587 * g + 0.114 * b)
#         r, g, b = y, y, y
#
#         pixels[i, j] = (r, g, b)
#
#
#
# img.show()

# import colorsys
#
# from PIL import Image
# img = Image.open("lenna.png") # must be in same folder
# width, height = img.size
# pixels = img.load()
#
# for i in range(width):
#     for j in range(height):
#         r, g, b = pixels[i, j]
#
#         y = int(0.25 * r + 0.25 * g + 0.25 * b)
#
#         # colorsys uses colors in the range [0, 1]
#         h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
#
#         h = float(h)
#         h += .10
#         s = float(s)
#         s += 0.10
#         v = float(v)
#         v += 0.10
# x
#         r, g, b = colorsys.hsv_to_rgb(h, s, v)
#
#         # convert back to [0, 255]
#
#         r = int(r * 255)
#         g = int(g * 255)
#         b = int(b * 255)
#
#         # your code here
#
#         pixels[i, j] = (r, g, b)
#
# img.show()



from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (40, 77)), fill="red")

# draw a rectangle from x0, y0 to x1, y1
draw.rectangle(((0, 0), (300, 300)), fill="lightblue")

# draw a line from x0, y0, x1, y1
# using the color pink
color = (256, 128, 128)  # pink
draw.line((1, 10, width, height), fill='red')
draw.line((1, height, width, 1), fill='red')


circle_x = width/1
circle_y = height/1
circle_radius = 100
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')

img.show()