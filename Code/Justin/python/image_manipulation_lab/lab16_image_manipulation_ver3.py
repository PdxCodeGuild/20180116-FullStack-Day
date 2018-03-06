from PIL import Image, ImageDraw

# Draw a stick figure
width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)

# Draw head
draw.ellipse((200, 50, 300, 150), outline = "blue", fill='lightgreen')

# Draw a body
draw.line((250, 150, 250, 350), width = 10, fill = "red")

# Draw arms
draw.line((250, 200, 300, 150), width = 10, fill = "red")
draw.line((250, 200, 200, 150), width = 10, fill = "red")

# Draw legs
draw.line((250, 350, 350, 450), width = 10, fill = "red")
draw.line((250, 350, 150, 450), width = 10, fill = "red")

img.show()
