import random
answer = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it',
          'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again',
          'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
          'Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good,', 'Very doubtful']
final = random.choice(answer)
print('Welcome')
user_question = input('Ask a question. ')
output = final
print(output)
cont = input('Do you wish to ask another question? ')
while cont == 'yes':
    user_question = input('Ask a question. ')
    print(output)
    cont = input('Do you wish to ask another question? ')
else:
    print('Thank you.')
