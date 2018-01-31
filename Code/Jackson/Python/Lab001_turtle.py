"""
First lab drawing a stick figure
"""

#stick figure going up stairs

from turtle import *

setposition(0, 0)

fillcolor('red')
begin_fill()

i = 0
while i < 360:
    forward(1)
    left(1)
    i += 1

end_fill()

right(90)
forward(100)

right(90)
forward(100)
right(180)
forward(200)
right(180)
forward(100)
left(90)
forward(100)

right(45)
forward(100)
right(180)
forward(100)
right(90)
forward(100)


right(135)

i = 0
while i < 4:
	forward(100)
	left(90)
	forward(100)
	right(90)
	i = i + 1

done()



