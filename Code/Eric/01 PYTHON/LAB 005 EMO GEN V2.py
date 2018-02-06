#EMO GENERATOR (*5)
import random

#face lists
eyes_list = ['8', ':', ';', '=', 'B', '>:']
nose_list = [ '.', '^']
mouth_list = [')', '(', '@', ']', '$', '|']

#print random emoji 5 times:
i = 0
while i < 5:
	i += 1
	print('\n' + random.choice(eyes_list) + random.choice(nose_list) + random.choice(mouth_list))
