# Credit Card Project
def check_card(credit_card):

    is_valid = False

    #I created a list() and inside the list i use a map
    # the map makes credit card into a ints and since its inside
    # my list method then it makes the numbers into their own value
    credit_card_int = list(map(int,credit_card))

    #.pop() will remove the last number of the list. And the list will be
    # updated automatically without the removed digit.
    check_digit = credit_card_int.pop()


    # [::-1] reverses the entire number and store it in rev_digits
    # even if you remove from the credit_card_int after this it won't
    # change the value of rev_digits.
    rev_digits = credit_card_int[::-1]


    sum_of_credit_card = 0

    #THis code is commented because it is the same as the code that follows
    # but i was practicing list comprhension.

    # for index, value in enumerate(rev_digits):
    #     if index % 2 == 0:
    #         rev_digits[index] *= 2


    rev_digits = [rev_digits[i] * 2 if i % 2 == 0 else rev_digits[i] for i in range(len(rev_digits))]


    # Adds all values into sum.
    for x in rev_digits:
        if x > 9:
            sum_of_credit_card += x - 9
        else:
            sum_of_credit_card += x

    # Checks to see if check digit is in the sums. Since i coverted it to a string
    # it will access sum_of_credit_card by index.
    if str(check_digit) in str(sum_of_credit_card):
        is_valid = True

    return is_valid

credit_card = '4556737586899855'


if check_card(credit_card):
    print('Valid!')
else:
    print('Not Valid!')


