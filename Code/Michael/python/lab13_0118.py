


original = "abcdefghijklmnopqrstuvwxyz"
shifted = "nopqrstuvwxyzabcdefghijklm"

stringed = input('> ')

translation = stringed.maketrans(original, shifted)

print("Translated:", stringed.translate(translation))