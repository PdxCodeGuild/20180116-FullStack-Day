import random
yourChoice = int(input("1=rock, 2=paper, 3=scissors. enter your choice:"))
compChoice = random.randint(1,3)




def  win(yC, cC):
    if yC==1 and cC==3:
        return "win"
    if yC==1 and cC==2:
        return "lose"
    if yC==1 and cC==1:
        return "same"
    if yC==2 and cC==3:
        return "lose"
    if yC==2 and cC==1:
        return "win"
    if yC==2 and cC==2:
        return "same"
    if yC==3 and cC==1:
        return "lose"
    if yC == 3 and cC ==2:
        return "win"
    if yC == 3 and cC ==3:
        return "same"

resul = win(yourChoice, compChoice)

if yourChoice==1:
    yourChoice="rock"
elif yourChoice==2:
    yourChoice= "paper"
elif yourChoice==3:
    yourChoice= "scissors"

if compChoice==1:
    compChoice="rock"
elif compChoice==2:
    compChoice= "paper"
elif compChoice==3:
    compChoice= "scissors"

print("your choice is " + yourChoice+ " computer's choice is "+ compChoice + " the result is "+ resul)