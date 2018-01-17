
# Practice: Strings

## Problem 1

Get a string from the user, print out another string, doubling every letter.

```
>>> Enter some text: hello
hheelloo
```

## Problem 2

Write a function that takes a string, and returns a list of strings, each missing a different character.

```python
missing_char('kitten') → ['itten', 'ktten', 'kiten', 'kiten', 'kittn', 'kitte']
```

## Problem 3
Return the letter that appears the latest in the english alphabet.
```
>>> latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')
the latest letter is v.
```

## Problem 9

Write a function that returns the number of occurances of 'hi' in a given string.

```python
count_hi('hihi') → 2
```

## Problem 10

Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'

```python
cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('catdogcatdog') → True
```




## Problem 7
Return the number of letter occurances in a string.
```python
def count_letter(letter, word):
    ...
count_letter('i', 'antidisestablishmentterianism') → 5
count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis') → 2
```

## Problem 8

Convert input strings to lowercase without any surrounding whitespace.

```
lower_case("SUPER!") → 'super!'
lower_case("        NANNANANANA BATMAN        ") → 'nannananana batman'
```
