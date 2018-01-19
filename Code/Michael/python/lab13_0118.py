


original = "abcdefghijklmnopqrstuvwxyz"
# originalupper = original.upper()

shifted = "nopqrstuvwxyzabcdefghijklm"

stringed = input('> Type something you fool!\n> ')

translation = stringed.maketrans(original, shifted)

print("Translated:", stringed.translate(translation))