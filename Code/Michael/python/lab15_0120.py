
aughts = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}
teens = {5: 'teen'}
doubles = {2: 'twenty', 3: 'thirty', 4: 'forty'}

x = 67

tens_digit = x // 10
ones_digit = x % 10

if tens_digit == 6:
    sixty = str(tens_digit)
    tens_digits = sixty

print(tens_digits, ones_digit)