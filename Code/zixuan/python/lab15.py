hour = int(input("input hour:"))
min = int(input("input min:"))

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
    return word

hour_1 = int(hour/10) * 10
hour_2 = int(hour % 10)
hour_1 = inttostr(hour_1)
hour_2 = inttostr(hour_2)
hour = hour_1+"-"+hour_2

print(hour)

