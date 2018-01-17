import random


#Make lists of eyes, nose, and mouths of the emoticons
eyes = [':', ';', '8', 'X']
nose = ['^', '', '-']
mouth = ['(', ')', 'D', '/', '\\']

print(random.choice(eyes), random.choice(nose), random.choice(mouth), sep='')