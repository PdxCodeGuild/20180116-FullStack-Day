"""
This program will take the png skies that have been cropped and turns them into prints that will be uploaded to dropbox
"""
from PIL import Image
import datetime, os.path

# variable that will change
date = datetime.date(2018, 1, 16)  # starting date
diary = 146
current_image = 1020084  # last 7 digits after the 'P', will change with new camera
ending_image = 1020190
folder_path = "/Users/jacksonreed/Desktop/v2 Sky Diary - Proofs/" + str(diary) + "/JPEG/"  # should be able to shorten


while current_image <= ending_image:
    im_path = folder_path + str(date) + "_" + str(current_image) + ".png"
    if os.path.isfile(im_path):
        canvas_width = 1350  # 1350x1950 were sizes of png files sent to Blicks
        canvas_height = 1950
        canvas = Image.new('RGB', (canvas_width, canvas_height), (255, 255, 255))
        sky = Image.open(im_path)
        sky_width, sky_height = sky.size
        # resize image and paste on canvas
        y = int((canvas_width * sky_height) / sky_width)
        im = sky.resize((canvas_width, y), Image.ANTIALIAS)
        canvas.paste(im, (0, 0, canvas_width, y))

        # add the stamps.  Note: the max image is 450 x 150... need 600px at bottom = 3x100 + 150x2
        # add month
        month_im = Image.open("/Users/jacksonreed/Desktop/dates/month" + str(date.strftime('%m')) + ".png")
        month_width, month_height = month_im.size
        padding = 100
        month_x = int(canvas_width / 2) - (padding + month_width)
        month_y = y + padding
        canvas.paste(month_im, (month_x, month_y, (month_x + month_width), (month_y + month_height)))

        # add day
        day_im = Image.open("/Users/jacksonreed/Desktop/dates/day" + str(date.strftime('%d')) + ".png")
        day_width, day_height = day_im.size
        # Need to test this !!! Trying to get the shorter days to look better
        if int(date.strftime('%d')) < 10:
            x_padding = 166
        else:
            x_padding = 100
        day_x = int(canvas_width / 2) + x_padding  # added a second padding to make it look more even
        day_y = y + padding
        canvas.paste(day_im, (day_x, day_y, (day_x + day_width), (day_y + day_height)))

        # add year
        year_im = Image.open("/Users/jacksonreed/Desktop/dates/year" + str(date.strftime('%Y')) +".png")
        year_width, year_height = year_im.size
        padding = 100
        year_x = int((canvas_width / 2) - (year_width / 2))
        year_y = y + padding + 225  # changed to 225250 is padding above day/month and day/month_height
        canvas.paste(year_im, (year_x, year_y, year_x + year_width, year_y + year_height))

        # save file into new folder
        canvas.save("/Users/jacksonreed/Desktop/skies_png/" + str(date) + ".png", "PNG")
        # increment date only when image is created to account for deleted image numbers on camera
        date += datetime.timedelta(days=1)
    current_image += 1