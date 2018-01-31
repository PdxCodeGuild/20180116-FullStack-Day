
card = list(input('Please input your 16 digit card number: '))
check = []
check.append(card[15])
print(check)
del card[15]
card.reverse()
print(card)
for i in range(len(card)):
    if i % 2 == 0:
        card[i] = int(card[i]) * 2
    else:
        card[i] = int(card[i])

for i in range(len(card)):
    while card[i] > 9:
        card[i] -= 9

sumvalue = sum(int(i) for i in card)
[int(i) for i in [sumvalue]]
print(sumvalue) #value check



print(card)











