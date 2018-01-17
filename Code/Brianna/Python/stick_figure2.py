from turtle import *

"""
Making the head
"""

head = 0

while head < 18:
        forward(4)
        left(20)
        head = head + 1

""" 
Making the body and arms
"""

right(90)
forward(30)

"""
Making the arms 
"""

left(90)
forward(30)
left(45)
forward(30)
right(180)
right(45)
penup()
forward(80)
left(90)
pendown()
forward(30)
left(110)
forward(30)
right(90)

""" 
Starting on rest of torso and legs 
"""
forward(50)
right(120)
forward(40)
left(45)
forward(60)

"""
Finishing up the legs
"""
penup
right(180)
forward(60)
right(45)
forward(40)
pendown()

right(90)
forward(50)
left(30)
forward(60)


done()
