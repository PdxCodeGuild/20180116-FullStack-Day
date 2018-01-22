
number = 37
zero_to_ten = {0:'Zero', 1:'one', 2:'two', 3:'three',4:'four',5:'five',
               6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}

eleven_to_nineteen = {11:'eleven', 12:'twelve', 33:'thirteen',14:'fourteen',15:'fifteen',
               16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}

twenty_to_ninty = {20:'twenty', 30:'thirty',40:'fourty',50:'fifty',
               60:'sixty',70:'seventy',80:'eighty',90:'ninety'}


if number >= 100:
    print('I didnt go that far in making name for past the one hundreds')


if number >= 20 and number < 100:
    x = 10 * (number // 10)
    i = number % 10

    if i == 0:
        print(twenty_to_ninty[x])
    else:
        print(twenty_to_ninty[x] + ' ' + zero_to_ten[i])

if 20 > number >= 0:
    if number > 10:
        print(eleven_to_nineteen[number])
    else:
        print(zero_to_ten[number])



