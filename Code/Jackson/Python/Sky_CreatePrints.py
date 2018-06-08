from PIL import Image

date_img = Image.open("home01.JPG")
area = (0, 0, 300, 277)  # added size of png to info found from cropping
im.paste(date_img, area)
# draw white area
width, height = im.size
print(width)
print(height)
footer = ImageDraw.Draw(im)
footer.rectangle(((0, height), (width, width + 500)), fill="white")