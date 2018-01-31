

# 4556737586899855

def validator():
    card = input('Enter your card\n> ')
    # print(type(card))

    numbers = []
    for i in range(len(card)):
        numbers.append(int(card[i]))

    # numbers = [int(card[i]) for i in range(len(card))]
    # print(numbers)

    lastDigit = numbers.pop()
    # print(lastDigit)
    # print(numbers)

    reversed = numbers[::-1]
    # print(reversed)

    doubled = reversed.copy()
    for i in range(0, len(reversed), 2):
        doubled[i] *= 2
    print(doubled)

    for i in range(0, len(doubled)):
        if doubled[i] > 9:
            doubled[i] -= 9
    minus_nine = doubled
    # print(minus_nine)

    sumCard = sum(minus_nine)
    # print(sumCard)

    secondDigit = str(sumCard)[1]
    secondDigit = int(secondDigit)

    if secondDigit == lastDigit:
        print('valid')
    else:
        print('nope')

validator()

