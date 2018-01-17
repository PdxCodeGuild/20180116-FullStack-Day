import random
magic_answers = ["Of course!", "Sorry... I really am.", "Try again. Bad question. You don't want to know.", "Yes, if you stand up right now.", "You should probably ask something else.","It's totally possible.","Maybe, the future is foggy.","Yes."]

running = True

while running == True:
    tell_me = input('Welcome to the Magic 8 ball! Think of a question and type "ask," otherwise, if you are finished, type "done." :-)\n:')
    if tell_me == "ask":
        print(random.choice(magic_answers))
    elif tell_me == "done":
        running = False
        print("See you another day!")
    else:
        print('Try again!')