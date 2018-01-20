digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
others = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

number = int(input('Input a number a number between 1 and 99: '))

if number < 0 or number > 99:
    number = input('Value is out of range. Please input a value between 1 and 99')
else:
    div = number // 10
    remain = number % 10

if div == 0:
    print(digits[remain - 1])
elif div == 1:
    print(others[remain])
elif 2 <= 9 and remain == 0:
    print(tens[div - 2])
else:
    print(tens[div - 2] + ' ' + digits[remain - 1])