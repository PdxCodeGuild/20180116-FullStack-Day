def check(card_num):
    card = []

    for nums in range(len(card_num)):
        card.append(int(card_num[nums]))
    check_num = card.pop()

    print(card)

    card.reverse()

    print(card)

    for i in range(0, len(card), 2):
        card[i] *= 2

    print(card)

    sum = 0

    for j in range(len(card)):
        if card[j] > 9:
            card[j] -= 9
        sum += card[j]

    print(card)

    print(sum)

    for digit in range(1, 10):
        if sum <= 10 * digit:
            f_check = sum % 10

    print(check_num)

    print(f_check)


    if f_check == check_num:
        print('Card is valid')
    else:
        print('Card is not vaild.')

    return


check('4556737586899855')