# Draw a stick figure

from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)

draw.rectangle(((0, 0), (width, height)), fill="white")
color = (200, 10, 200)
draw.line((250, 250, 250, 400), fill=color, width=5)
draw.line((250, 400, 300, 450), fill=color, width=5) #leg 1
draw.line((250, 400, 200, 450), fill=color, width=5)
draw.line((200, 300, 300, 300), fill=color, width=5)
circle_x = width/2
circle_y = height/2
circle_radius = 25
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill=color)

img.show()