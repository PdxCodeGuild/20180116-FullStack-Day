import random
print("Rock, Paper, Scissors: THE GAME")
c = ["rock", "paper", "scissors"]
while True:
    result = random.choice(c)
    u = input("Choose between rock, paper, and scissors\n:").lower()
    print(result)
    r = "rock"
    p = "paper"
    s = "scissors"
    w = "You win"
    l = "You lose"
    t = "It's a tie"
    if u == r:
        if result == r:
            print(t)
        if result == p:
            print(l)
        if result == s:
            print(w)
    if u == p:
        if result == r:
            print(w)
        if result == p:
            print(t)
        if result == s:
            print(l)
    if u == s:
        if result == r:
            print(l)
        if result == p:
            print(w)
        if result == s:
            print(t)
    a = input("Try again?\n:")
    if a.lower() == 'no':
        print("Good Bye!")
        break

