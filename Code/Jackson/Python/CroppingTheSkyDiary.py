from PIL import Image
import datetime

# enter a starting information
starting_date = datetime.date(2018, 1, 16)
diary = 146
current_image = 291
ending_image = 394
Folder_path = "/Users/jacksonreed/Desktop/146_TEST/JPEG/"
box = (1430, 450, 4200, 3170) #figure out looking at the first image, pixels: left, upper, right, lower

while current_image <= ending_image:

    im = Image.open("/Users/jacksonreed/Desktop/146_TEST/JPEG/P1000291.jpg")
    im = im.crop(box)
    im = im.rotate(90)
    im.save()

    current_image += 1
