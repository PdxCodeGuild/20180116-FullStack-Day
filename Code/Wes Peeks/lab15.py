# Dictionary variables
# single
single_num = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
              8: 'eight', 9: 'nine'}

# tens
ten_num = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty',
           9: 'ninety'}

# teens
teen_num = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
            18: 'eighteen', 19: 'nineteen'}

# hundreds
hundred_num = {1: 'one-hundred', 2: 'two-hundred', 3: 'three-hundred', 4: 'four-hundred', 5: 'five-hundred',
               6: 'six-hundred', 7: 'seven-hundred', 8: 'eight-hundred', 9: 'nine-hundred'}

# roman
romanI = {1: 'I', 2: 'II', 3: 'III'}
romanV = {4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII'}
romanX = {9: 'IX', 10: 'X', 11: 'XI', 12: 'XII', 13: 'XIII', 14: 'XIV', 15: 'XV', 16: 'XVI', 17: 'XVII', 18: 'XVIII',
          19: 'IX', 20: 'XX'}

# user input
num_input = int(input('Input Number.\n:'))


# if statements
if num_input == 0:
    print('zero')

elif num_input == 10:
    print('ten')

elif num_input < 10:
    x = num_input % 10
    print(single_num[x])

elif num_input > 10 and num_input < 20 and num_input in teen_num.keys():
    print(teen_num[num_input])

#elif num_input > 20 and num_input < 100:
elif 20 < num_input < 100:
    x = num_input % 10
    y = num_input // 10
    print(ten_num[y], single_num[x])


elif 100 < num_input < 1000:
    x = num_input % 100
    y = num_input // 100
    z = x % 10
    x = x // 10
    print(hundred_num[y], ten_num[x], single_num[z])







