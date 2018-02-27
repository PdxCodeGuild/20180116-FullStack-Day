import time

name = input('enter a name: ')
language = input('enter a programming language: ')
adjective = input('enter an adjective: ')
creature = input('enter an imaginary beast: ')
c_name = input('enter a name that is appropriate for an imaginary beast: ')
city = input('enter a faraway city: ')
print('Thank you... \nHere is you mad-lib.')

time.sleep(1)
print('Working...')
time.sleep(1)
print('Working...')
time.sleep(1)
print('Wait for it...')
time.sleep(1)
print("It's almost ready now.")
time.sleep(1)
print('Here it is...\n\n')
time.sleep(2)
print (f"This is {name}'s first {language} mad-lib.")
print (f"After this course is over {name} and his best {adjective}, {creature} friend, \n"
       f"named {c_name} are taking a vacation to {city}.")

