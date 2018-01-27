

# 4556737586899855

def validator():
    card = input('Enter your card\n> ')
    print(type(card))

    numbers = [int(card[i]) for i in range(len(card))]
    print(numbers)

    lastDigit = numbers.pop()
    print(lastDigit)
    print(numbers)

    reversed = numbers[::-1]
    print(reversed)

    for i in range(0, len(reversed), 2):
        reversed[i] *= 2
        doubled = reversed
        print(doubled)

    for i in range(0, len(doubled)):
        if doubled[i] > 9:
            doubled[i] -= 9
            minusNine = doubled
            print(minusNine)

    sumCard = sum(minusNine)
    print(sumCard)

    secondDigit = str(sumCard)[1]
    secondDigit = int(secondDigit)

    if secondDigit == lastDigit:
        print('valid')
    else:
        print('nope')

validator()

