"""
Pillow can also be used to draw, the code below demonstrates some functions that Pillow provides. Use these functions to draw a stick figure. You can find more documentation here.


"""


from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill="white") #background


# draw a line from x0, y0, x1, y1
# using the color pink
color = (256, 128, 128)  # pink
draw.line((100, 100, width/2, height/2), fill=color) #left arm
draw.line((width/2, height/2, 400, 100), fill=color) #right arm
draw.line((width/2, height/1.5, 300, 450), fill=color) #right leg
draw.line((width/2, height/1.5, 200, 450), fill=color) #left leg



## draw a rectangle from x0, y0 to x1, y1
draw.rectangle(((200, 200), (300, 350)), fill="lightblue")


circle_x = width/2
circle_y = height/4
circle_radius = 70
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')

img.show()