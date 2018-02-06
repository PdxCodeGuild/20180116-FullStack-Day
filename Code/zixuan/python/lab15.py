number = int(input("input number:"))


def inttostr (i):
    word = "zero"

    if i == 1:
        word = 'one'
    elif i == 2:
        word = 'two'
    elif i == 3:
        word = 'three'
    elif i == 4:
        word = 'four'
    elif i == 5:
        word = 'five'
    elif i == 6:
        word = 'six'
    elif i == 7:
        word = 'seven'
    elif i == 8:
        word = 'eight'
    elif i == 9:
        word = 'one'
    elif i ==10:
        word = 'ten'
    elif i == 11:
        word = 'eleven'
    elif i == 12:
        word = 'twelve'
    elif i == 20:
        word = 'twenty'
    elif i == 30:
        word = 'thirty'
    elif i == 40:
        word = 'forty'
    elif i == 50:
        word = 'fifty'
    elif i == 60:
        word = 'sixty'
    elif i == 70:
        word = 'seventy'
    elif i == 80:
        word = 'eighty'
    elif i == 90:
        word = 'ninety'
    elif i == 100:
        word = 'one humdred'
    elif i == 200:
        word = 'two humdred'
    elif i == 300:
        word = 'three humdred'
    elif i == 400:
        word = 'four humdred'
    elif i == 500:
        word = 'five humdred'
    elif i == 600:
        word = 'six humdred'
    elif i == 700:
        word = 'seven humdred'
    elif i == 800:
        word = 'eight humdred'
    elif i == 900:
        word = 'nine humdred'
    return word

number_1 = int(number/100) * 100
number_2 = int((number-number_1) / 10)*10
number_3 = int(number-number_1-number_2)

number_1 = inttostr(number_1)
number_2 = inttostr(number_2)
number_3 = inttostr(number_3)



print(number_1+"-"+number_2+"-"+number_3)

