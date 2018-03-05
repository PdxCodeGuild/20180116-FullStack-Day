import re
import nltk.corpus

wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]

lst = [w for w in wordlist if re.search('ed$', w)]
print(lst)

lst = [w for w in wordlist if re.search('^..j..t..$', w)]
print(lst)

lst = [w for w in wordlist if re.search('^[jkl][ghi][mno][def]$', w)]
print(lst)

lst = [w for w in wordlist if re.search('^.+[z]{2}.+$', w)]
print(lst)

lst = [w for w in wordlist if re.search('^.+[z]{2}.*(ed|ing)$', w)]
print(lst)

print([int(n) for n in re.findall('[0-9]+', '2009-12-31')])