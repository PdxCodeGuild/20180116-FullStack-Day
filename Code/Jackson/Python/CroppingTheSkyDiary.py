from PIL import Image, ImageEnhance  # brightness and contrast
import datetime
import os.path

# enter a starting information
starting_date = datetime.date(2018, 1, 16)
diary = 146
current_image = 291
ending_image = 295
folder_path = "/Users/jacksonreed/Desktop/146_TEST/JPEG/"  # update to take out "146_TEST/JPEG"
image_prefix = "P1000"
upperleft_x = 1430
upperleft_y = 450
lowerright_x = 4200
lowerright_y = 3170

box = (1430, 450, 4200, 3170)  # figure out looking at the first image, pixels: left, upper, right, lower
box =
# !!!Turn off Image Enhancer below if not needed!!!


# Start of program
while current_image <= ending_image:
    image_path = folder_path + image_prefix + str(current_image) + ".jpg"
    # check to see if path exists
    if os.path.isfile(image_path):
        im = Image.open(image_path)
        im = im.crop(box)
        im = im.rotate(90)  # all photos taken with GH2 were done from the side.
        # *** Turn off if no added brightness is needed, i.e. version 2 folder
        enhancer = ImageEnhance.Brightness(im)
        im = enhancer.enhance(1.4)

        # Get Date Added Test
        date_img = Image.open("home01.JPG")
        area = (0, 0, 300, 277)  # added size of png to info found from cropping
        im.paste(date_img, area)
        # Test
        im.show()  # this is a good way to check that it's working

        # im.save()
    current_image += 1

