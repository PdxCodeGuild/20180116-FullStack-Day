import random

predictions = ['Yes', 'Absolutely', 'Hell yeah!', 'No', 'Maybe', 'Looks grim', 'Never', 'Definitely maybe', 'Hell no',
'Looking good!', 'Meh', 'Be more specific...', 'What do you REALLY want?', 'BRB', 'Out to Brunch...', 'Strong possibility']

print('\n Welcome to the Magic 8 Ball!\n I know many things... \n\n Type "stop" when you wish to discontinue.\n')
while True:
    user_input = input('\nWhat would you like to know?\n\n:')
    if user_input.lower() == 'stop':
        print('Goodbye!')
        break
    if '?' in user_input.lower():
        print(random.choice(predictions) + '\nYou may ask another question or type "stop" to discontinue.\n')
    else:
        print('\nPlease include a question mark!')
