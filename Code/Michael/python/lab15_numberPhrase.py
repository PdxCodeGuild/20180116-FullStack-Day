




def min(a, b):
    return a if a < b else b



def numbers(x):

    ones = {0: 'Zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    teens = {0: 'ten', 1: 'eleven', 2: 'twelve', 3: 'thirteen', 4: 'fourteen', 5: 'fifteen', 6: 'sixteen', 7: 'seventeen', 8: 'eighteen', 9: 'nineteen'}
    tens = {2: 'twenty', 3: 'thirty', 4: 'fourty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
    hundreds = {1: 'one-hundred', 2: 'two-hundred', 3: 'three-hundred', 4: 'four-hundred', 5: 'five-hundred', 6: 'six-hundred', 7: 'seven-hundred', 8: 'eight-hundred', 9: 'nine-hundred'}

    hundred = x // 100
    ten = x // 10 % 10
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

numbers(625)

