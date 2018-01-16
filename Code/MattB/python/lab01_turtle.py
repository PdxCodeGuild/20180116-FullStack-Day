from turtle import*

#Set size (perimeter) of circle
P = 270.0

#Angle size
angle = 360/P
perimeter = P/360

#Draw Head
fillcolor('blue')
begin_fill()

i = 0
while i < P:
    forward(perimeter)
    left(angle)
    i = i + 1

end_fill()

#Neck
right(90)
forward(20)

#Right arm
left(120)
forward(50)
penup()
left(180)
forward(50)
pendown()

#Left arm
right(60)
forward(50)
penup()
left(180)
forward(50)
pendown()

#Torso
right(60)
forward(60)

#Right Leg
left(20)
forward(50)
penup()
left(180)
forward(50)
pendown()

#Left leg
left(140)
forward(50)

done()