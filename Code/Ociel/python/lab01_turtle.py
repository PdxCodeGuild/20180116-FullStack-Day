<<<<<<< HEAD
from turtle import *

# draw head

edge_length = 200
n_sides = 100

i = 0
while i < n_sides:
	forward(edge_length/n_sides)
	left(360/n_sides)
	i = i + 1

# draw body and arms

right(90)
forward(25)
left(90)
forward(25)
left(180)
forward(50)
left(180)
forward(25)
right(90)
forward(75)

# draw legs

right(45)
forward(50)
right(180)
forward(50)
right(90)
forward(50)


done()


=======
"""
Lab 01: Turtle

"""

from turtle import *


#head
i = 1
while i < 37:
    forward(10)
    left(10)
    i = i + 1


#neck
right(90)
forward(20)


# right arms
left(90)
forward(150)


# left arm
left(180)
forward(300)
left(180)
forward(150)
right(90)

#body
forward(100)


#right leg
left(40)
forward(150)
left(180)
forward(150)


#left leg
left(40)
forward(170)
left(180)
forward(170)



















done()
>>>>>>> origin/master
