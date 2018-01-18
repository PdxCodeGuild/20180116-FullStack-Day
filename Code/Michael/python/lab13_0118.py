


original = "abcdefghijklmnopqrstuvwxyz"
shifted = "nopqrstuvwxyzabcdefghijklm"

string = input('> ')

translation = string.maketrans(original, shifted)

print("Translated:", string.translate(translation))