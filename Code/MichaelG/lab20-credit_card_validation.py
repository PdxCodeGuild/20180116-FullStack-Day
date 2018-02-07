
card = list(input('Please input your 16 digit card number: '))
check = []
check.append(card[15])
print(check) #make sure last digit was appended to new list
del card[15]
card.reverse()
print(card) #make sure removing last digit and reversal of list worked
for i in range(len(card)):
    if i % 2 == 0:
        card[i] = int(card[i]) * 2
    else:
        card[i] = int(card[i])
for i in range(len(card)):
    while card[i] > 9:
        card[i] -= 9

sumvalue = sum(int(i) for i in card)
sumstr = [int(i) for i in str(sumvalue)]

print(sumstr) #value check
if int(check[0]) == sumstr[1]:
    print('Card valid.')
else:
    print('Card not valid.')
