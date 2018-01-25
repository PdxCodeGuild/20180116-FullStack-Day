"Lab 1: Turtle"
"Stick Figure"
from turtle import *
from PIL import Image, ImageDraw
#move_distance = 100
#turn_angle =  144


#head
fillcolor('gray')
begin_fill()
circle(80)
end_fill()

#neck
right(90)
forward(30)

#arms
left(90)
forward(150)
left(90)
left(90)
forward(300)
left(90)
left(90)
forward(150)
right(90)
#start body
forward(175)
#legs
right(45)
forward(100)
right(180)
forward(100)
right(90)
forward(100)

done()