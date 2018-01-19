def tens(number):

    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    others = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
              'nineteen']
    div = number // 10
    remain = number % 10

    if div == 0:
        x = digits[remain - 1]
    elif div == 1:
        x = others[remain]
    elif 2 <= 9 and remain == 0:
        x = tens[div - 2]
    else:
        x = tens[div - 2] + ' ' + digits[remain - 1]
    return x

ones = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
num = int(input('Input a number between 100 and 999: '))

if num < 100 or num > 999:
    num = input('Number is out of range, please input a number between 100 and 999: ')
else:
    h_div = num // 100
    h_remain = num % 100

if num == 100:
    print('One hundred')
else:
    y = tens(h_remain)
    print(f'{ones[h_div - 1]} hundred and {y}')
