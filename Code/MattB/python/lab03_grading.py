score = int(input('What is your score?: '))

#find number in one's place
ones = score%10

#find symbol for score
if 0 <= ones < 4:
    symbol = '-'
elif 7 <= ones <= 9:
    symbol = '+'

if score == 100:
    print('A+')
elif 90 <= score <= 99:
    print('A', symbol, sep='')
elif 80 <= score <= 89:
    print('B', symbol, sep='')
elif 70 <= score <= 79:
    print('C', symbol, sep='')
elif 60 <= score < 70:
    print('D', symbol, sep='')
else:
    print('F')
