import turtle
from turtle import *

#squarehead
setposition(0, 0)

forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
penup()

#body
setposition(25, 0)
pendown()
right(90)
forward(150)

#leg 1
left(35)
forward(120)
penup()

#leg 2
setposition(25, -150)
pendown()

right(70)
forward(120)
penup()

#arm 1
setposition(25, -40)
pendown()

forward(100)
penup()

#arm 2
setposition(25, -40)
pendown()

left(70)
forward(100)
penup()

turtle.done()
