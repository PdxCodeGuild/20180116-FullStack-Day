from turtle import *

scale = 100

fillcolor('red')

# legs
left(60)
forward(100)
right(120)
forward(100)
left(180)
forward(100)
left(-30)
forward(100)

# arms
left(60)
forward(100)
left(180)
forward(100)
right(-60)
forward(100)
left(180)
forward(100)

# neck
left(-120)
forward(50)

from turtle import *

edge_length = 0
i = 0
while i < 100:
	forward(edge_length)
	right(144)

	edge_length += 4

done()


end_fill()

done()