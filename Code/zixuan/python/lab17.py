your_word = input("please enter your word:")
x = 'ara'


def Palindrome(s):
    if len(s) % 2 == 1:
        start_index = int((len(s) / 2))
        for i in range(0, int(len(s) / 2)):
            if s[start_index + i] != s[start_index - i]:
                return False
        return True

    if len(s) % 2 == 0:
        start_index = int((len(s) / 2)) - 1
        for i in range(0, int(len(s) / 2)):
            if s[start_index + 1 + i] != s[start_index - i]:
                return False
        return True


print(Palindrome(your_word))
