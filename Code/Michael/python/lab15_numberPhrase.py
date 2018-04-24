




def min(a, b):
    return a if a < b else b



def numbers(x):

    ones = {0: 'Zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    tens = {20: 'twenty', 30: 'thirty', 40: 'fourty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
    hundreds = {100: 'one-hundred', 200: 'two-hundred', 300: 'three-hundred', 400: 'four-hundred', 500: 'five-hundred', 600: 'six-hundred', 700: 'seven-hundred', 800: 'eight-hundred', 900: 'nine-hundred'}

    hundred = x // 10 * 10 * 10
    ten = x // 10 * 10
    one = x % 10

    text = ""


    if x <= 10:
        text = ones[one]

    if x >= 10 and x <= 19:
        text = teens[x]

    if x >= 20 and x <= 99:
        text = tens[ten] + '-' + ones[one]

    if x >= 100 and x <= 999:
        text = hundreds[hundred] + '-' + tens[ten] + '-' + ones[one]

    print(text)


numbers(65)

