import random

shake = ["Maybe", "Yes", "Stop Shaking Me."]

while True:
    question = input("Ask a question?\n:")
    if question == 'quit':
        break
    else:
        print(random.choice(shake))
