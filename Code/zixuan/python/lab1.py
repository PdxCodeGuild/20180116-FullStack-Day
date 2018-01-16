from turtle import *

setposition(0,0)
setposition(0,100)
penup()
setposition(0,0)
pendown()
setposition(-40,-30)
penup()
setposition(0,0)
pendown()
setposition(40,-30)
penup()
setposition(0,90)
pendown()
setposition(-30,70)
penup()
setposition(0,90)
pendown()
setposition(30,70)
penup()
setposition(0,100)
pendown()



edge_length = 200
n_sides = 200

i = 0
fillcolor('red')
begin_fill()
while i < n_sides:

	forward(edge_length/n_sides)
	left(360/n_sides)
	i = i + 1
end_fill()
done()

