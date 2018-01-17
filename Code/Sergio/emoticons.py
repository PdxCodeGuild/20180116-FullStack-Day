#from Solutions on Github
import random

def create_emoticon():

    list_eyes = [':' , '8', ';' , ':::']
    list_noses = ['v' , '^' , '*' , '.' , ',']
    list_mouths = [')' , '(' , '|' , 'C' , '/']

    eyes = random.choice(list_eyes)
    nose = random.choice(list_noses)
    mouth = random.choice(list_mouths)

    emoticon = eyes + nose + mouth

    return emoticon


for i in range(5):
    print(create_emoticon())

#  my non-working code
# import random
#
# emoticon_eyes = [':' , '8', ';' , ':::']
# emoticon_mouth = [')' , '(' , '|' , 'C' , '/']
# emoticon_nose = ['v' , '^' , '*' , '.' , ',']
#
# emoticon = (random.choice(emoticon_eyes) + random.choice(emoticon_nose) + random.choice(emoticon_mouth))
#
# counter = 0
# while counter < 5:
#     print(emoticon)
#     counter = counter + 1



#------------------------------------------------
#first attempt
# count = 0
# while (count < 4):
#    print(emoticon)
#    count = count + 4
