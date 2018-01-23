

from turtle import *
# Draw head and make it red
fillcolor('red')
begin_fill()
circle(50)
end_fill()

# Draw neck
right(90)
forward(75)

# Draw arms
left(120)
forward(50)
left(180)
forward(50)
right(60)
forward(50)
right(180)
forward(50)

# Draw body
right(60)
forward(50)

# Draw legs
left(30)
forward(50)
left(180)
forward(50)
left(120)
forward(50)
left(180)
forward(50)

done()