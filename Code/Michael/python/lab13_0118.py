


original = "abcdefghijklmnopqrstuvwxyz"
shifted = "nopqrstuvwxyzabcdefghijklm"

stringed = input('> Type something you fool!\n> ')

translation = stringed.maketrans(original, shifted)

print("Translated:", stringed.translate(translation))