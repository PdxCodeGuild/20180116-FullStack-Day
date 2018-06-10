"""
Take JPEGs (Photoshop can convert RAW files, see The Sky Diary Instructions) and create a png ready to print, but with
the original image still in the name so review and to use for other purposes.
Another program will take all these images and create proofs and final versions.
"""
from PIL import Image, ImageEnhance
import datetime
import os.path


# variable that will change
starting_date = datetime.date(2018, 1, 16)
diary = 146
current_image = 1020084  # last 7 digits after the 'P', will change with new camera
ending_image = 1020190
folder_path = "/Users/jacksonreed/Desktop/v2 Sky Diary - Proofs/" + str(diary) + "/JPEG/"  # should be able to shorten
image_prefix = "P"  # this will change with the new camera
# figure out pixels by looking at first one.  Make sure ratio will allow at least 600 pixels at the bottom
upperleft_x = 1420
upperleft_y = 336
lowerright_x = 4228
lowerright_y = 3125
enhance = False  # for version_2 folder, this doesn't need to happen


# other variables that shouldn't change
box = (upperleft_x, upperleft_y, lowerright_x, lowerright_y)

# Start of program
while current_image <= ending_image:
    image_path = folder_path + image_prefix + str(current_image) + ".jpg"
    # check to see if path exists
    if os.path.isfile(image_path):
        im = Image.open(image_path)
        im = im.crop(box)
        im = im.transpose(Image.ROTATE_90)  # all photos taken with GH2 were done from the side.
        if enhance:
            enhancer = ImageEnhance.Brightness(im)
            im = enhancer.enhance(1.4)
        # Save with date added
        im.save(folder_path + str(starting_date) + "_" + str(current_image) + ".png", "PNG")
        # increment date at the end
        starting_date += datetime.timedelta(days=1)
        # im.show()  # this is a good way to check that it's working
    current_image += 1
