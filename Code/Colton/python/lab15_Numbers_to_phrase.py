ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['','', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety',]


while True:
    try:
        user = int(input("Give a number in numerical form\n:"))
        tens_digit = (user) // 10
        ones_digit = (user) % 10
    except ValueError:
        continue
    else:
        break
def get_tens_phrase(user):
    if user < 10:
        return ones[user]
    elif user < 20:
        return teens[user - 10]
    elif user < 100:
        tens_digit = user // 10
        ones_digit = user % 10
        if ones_digit == 0:
            return tens[tens_digit]
        else:
            return tens[tens_digit] + '-' + ones[ones_digit]


if user < 100:
    print(get_tens_phrase(user))



