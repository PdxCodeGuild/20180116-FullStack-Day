from PIL import Image, ImageDraw
from random import randint

width = 500
height = 500

img = Image.new('RGB', (width, height,))
draw = ImageDraw.Draw(img)

circle_x = width / 2
circle_y = height / 4
circle_radius = 50
draw.ellipse((circle_x - circle_radius, circle_y - circle_radius, circle_x + circle_radius, circle_y + circle_radius),
             fill='lightgreen')

# draw a rectangle from x0, y0 to x1, y1  # stick body
draw.rectangle(((249, 173), (251, 250)), fill="lightblue")

# draw a horizontal rectangle from x0, y0 to x1, y1  # arms
draw.rectangle(((300, 190), (200, 195)), fill="lightgreen")


# draw a line from x0, y0, x1, y1 # right leg
# using the color pink
color = (255,255,255)  # white
draw.line((250, 250, 300, 300), fill=color)
# right leg
# using the color pink
draw.line((0, height, width, 0), fill=color)

img.show()