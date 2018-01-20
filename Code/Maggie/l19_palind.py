#Palindrome checker

# test words
w1 = 'racecar'
w2 = 'palindrome'
r_str = ''
# first iterate through a string

print(w2[::-1])

def eval_pal(word): # returns boolean palindrome or no?
    return word[::-1] == word

print(eval_pal(w2))