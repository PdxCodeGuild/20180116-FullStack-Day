import random

mylist = ["it is certain", "it is decidedly", "without a doubt",
          "Yes Definetly", " You may rely on it", "As i see it, yes",
          "Most Likely", "OutLook good", "Yes", "Signs point to Yes",
          "Reply hazy try again", " Ask again Later", "Better not tell you now",
          "Cannot predict now", "Concentrate and ask again", "Don't Count on it",
          "My reply is No", "My sources say no", "Outlook not so good", "Very Doubtful"]

print("Welcome User! ")
userReply = True

while userReply != 'no':
    input("Please ask me a question and i will predict the outcome: ")
    print(random.choice(mylist))
    userReply = input("would you like to play again?")

print("Thank you for playing")

