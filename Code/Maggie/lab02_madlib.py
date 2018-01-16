'''
Madlibs
'''

a = 'an adjective'
p = 'a place'
n = 'a noun'
pln = 'a plural noun'
v = 'a verb'
num = 'a number'
b = 'a body part'
g = 'a group of people'

def query(wtype):
    'Input ' + wtype + ': '


q1 = str(query(v))
q2 = str(query(n))
q3 = str(query(g))

print('10 ways to {word_1} your {word_2}. {word_3} hate them, find out why!'.format(word_1=input(q1), word_2=input(q2), word_3=input(q3)))

