"""
Lab 19: Unit Converter. Grams to micrograms. :P
"""
#  use float for precision
grams = float(input("Enter the number of grams to convert into micrograms:\n"))

#  gram (key), microgram (value)
unit_dict = {'gram': 1, 'micrograms': 1000000}
def gram_to_micrograms(gram):
    microgram = gram * unit_dict['micrograms']
    return microgram


print(gram_to_micrograms(grams))
