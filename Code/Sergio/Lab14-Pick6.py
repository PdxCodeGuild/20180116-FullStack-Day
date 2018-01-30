"Lab 14: Pick6"
import random



# def add(a, b):
#     return a + b
#
# x = 5
# print(add(x, 4))



def matches(lottery, ticket):
    matches = 0
    for i in range(0, 6):
        if lottery[i] == ticket[i]:
            matches += 1
    return matches




def pick6():
    nums = []
    for i in range(6):
        num = random.randint(1, 99)
        nums.append(num)
    return nums



lottery = pick6()
print('Lottery numbers: ')
print(lottery)

ticket = pick6()

print('Your lottery numbers: ')
print(ticket)


m = matches(lottery, ticket)


#  not done



