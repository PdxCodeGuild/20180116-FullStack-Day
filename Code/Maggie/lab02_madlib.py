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

print('let\'s try a madlib! \nFollow the instructions below.')
q1 = input('Input ' + v + ': ')
q2 = input('Input ' + n + ': ')
q3 = input('Input ' + pln + ': ')

print('10 ways to {word_1} your {word_2}. {word_3} hate them; find out why!'.format(word_1=q1, word_2=q2, word_3=q3))

