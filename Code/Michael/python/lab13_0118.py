


original = "abcdefghijklmnopqrstuvwxyz"
originalupper = original.upper()

shifted = "nopqrstuvwxyzabcdefghijklm"

stringed = input('> ')

translation = stringed.maketrans(original, shifted)

print("Translated:", stringed.translate(translation))