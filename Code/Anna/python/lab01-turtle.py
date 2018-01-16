"""
Lab 1: Turtle
stick figure turtle is sticky
"""

from turtle import *

move_distance = 150
turn_around = 180

# torso
left(90)
forward(move_distance)
left(turn_around)
forward(250)

# legs
right(33)
forward(move_distance)
right(turn_around)
forward(move_distance)
right(57)
right(57)
forward(move_distance)
right(turn_around)
forward(move_distance)
right(33)

# arms
forward(move_distance)
right(50)
forward(100)
left(90)
forward(25) # fingers
left(turn_around)
forward(25)
left(70)
forward(25)
left(turn_around)
forward(25)
right(120)
forward(25)
left(turn_around)
forward(25)
left(90)
forward(25)
left(turn_around)
forward(25)
left(50)
forward(100)
right(-20) # arm 2
forward(100)
forward(25) # fingers
left(turn_around)
forward(25)
left(70)
forward(25)
left(turn_around)
forward(25)
right(120)
forward(25)
left(turn_around)
forward(25)
left(-90)
forward(25)
left(turn_around)
forward(25)
right(40) # return
forward(100)
left(30)
forward(100)

# head
penup()
forward(90)
left(90)
forward(90)
right(90)
right(turn_around)
pendown()
circle(90)

# eyes
left(90)
penup()
forward(45)
pendown()
circle(15)
penup()
forward(60)
left(90)
pendown()
circle(15)

# mouth
left(turn_around)
penup()
forward(60)
right(115)
forward(40)
pendown()
forward(60)

# draw, little turtle, draw!
done()