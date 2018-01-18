#BASIC EMO GENERATOR
import random

#face lists
eyes_list = ['8', ':', ';', '=', 'B', '>:']
nose_list = [ '.', '^']
mouth_list = [')', '(', '@', ']', '$', '|']

#print random:
print('\n' + random.choice(eyes_list) + random.choice(nose_list) + random.choice(mouth_list))
