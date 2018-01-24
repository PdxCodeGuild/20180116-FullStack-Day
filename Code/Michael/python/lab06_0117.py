import random

def randomizer(y):

    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*']
    #chars = 'abcdefgh0123456789ABCDD'
    # chars = list(chars)

    x = 0

    while x < y:
        x += 1
        ranstr = random.choice(chars)
        print(ranstr, end='')

randomizer(14)