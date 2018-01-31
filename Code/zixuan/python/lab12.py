import random
x =int( random.randint(1,10))

Diff = 10
def check (y):
    if y == x:
        return True
    if Diff > abs(x-y):
        print("closer")

    if Diff <= abs(x-y):
        print("not closer")


    return False



while True:
    y =int( input("please guess a number"))
    che = check(y)
    Diff = abs(x - y)
    if che == True:
        print("you are right!!!")
        break

