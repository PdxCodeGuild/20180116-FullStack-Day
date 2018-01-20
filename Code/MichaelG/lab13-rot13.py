import codecs

while True:
    inc = input('Please enter something to encode: ')
    enc = codecs.getencoder("rot-13")
    os = enc(inc)[0]
    output = os
    print(output)
    aga = input('Would you like to encode again? Yes or no.')
    if aga == 'no':
        break
    elif aga == 'yes':
        inc

print('Goodbye.')
