ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety',]




while True:
    try:
        user = int(input("Give a number in numerical form\n:"))
    except ValueError:
        continue
    else:
        break

input_tens_digit = (user) // 10
input_ones_digit = (user) % 10


print(input_tens_digit)
print(input_ones_digit)

