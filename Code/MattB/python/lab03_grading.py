score = int(input('What is your score?: '))

if 90 <= score <= 100:
    print('A')
elif 80 <= score <= 89:
    print('B')
elif 70 <= score <= 79:
    print('C')
elif 60 <= score < 70:
    print('D')
else:
    print('F')
