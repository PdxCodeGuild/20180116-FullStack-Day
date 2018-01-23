"""
Using a while loop, keep asking the user for a question, if they enter 'done', exit

"""
import random
a = True
while a == True:
    # Print a welcome screen to the user.
    print('Ask a question to the magic 8 ball or type "done" to stop')

    # Prompt the user to ask the 8-ball a question
    question1 = input('What would you like to know?: ')

    if question1 == 'done':
            break

    # Use the random module's random.choice() to choose a prediction.
    outcomes = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', \
                'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again', \
                'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', \
                'Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

    answer = random.choice(outcomes)

    # Display the result of the 8-ball.

    print(answer)