"""
This lab will involve writing a program that allows the user to convert a number between units.

"""

#get the user imput

meterinput = float(input('Enter a number of meters that you want converted to feet: '))

#conversion:  1 ft is 0.3048 m.

feetoutput = meterinput * .3048

print(str(feetoutput))

