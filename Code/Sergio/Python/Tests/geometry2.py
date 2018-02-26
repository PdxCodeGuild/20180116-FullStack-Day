from PIL import Image, ImageDraw
from random import randint
import string

width = 500
height = 500

img = Image.new('RGB', (width, height,))
draw = ImageDraw.Draw(img)




color = (255,255,255)  # white
# diagonal lines
draw.line((500, 0, 0, 500), fill=color) #bottom right to top left
draw.line((0, 0, 500, 500), fill=color) #bottom left to top right
draw.line((250, 0, 0, 250), fill=color) #middle left to middle top
draw.line((500, 250, 250, 0), fill=color) #middle top to middle right
draw.line((500, 250, 250, 500), fill=color) #middle right to middle bottom
draw.line((250, 500, 0, 250), fill=color) #middle bottom to middle left

draw.line((250, 0, 250, 250), fill=color) #middle bottom to middle left
draw.line((250, 0, 500, 250), fill=color) #middle bottom to middle left
draw.line((250, 0, 500, 500), fill=color) #middle bottom to middle left
draw.line((250, 0, 250, 500), fill=color) #middle bottom to middle left

draw.line((0, 0, 250, 500), fill=color) #middle bottom to middle left
draw.line((250, 0, 0, 500), fill=color) #middle bottom to middle left




# horizontal
draw.line((500, 250, 0, 500), fill=color) # horizontal line in middle
# vertical
draw.line((250, 500, 500, 0), fill=color) # top to bottom in middle
draw.line((0, 500, 500, 250), fill=color) # top to bottom in middle









img.show()
