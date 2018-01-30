# Regular Expressions in Python

You can find out more about regular expressions [here](https://docs.python.org/3.6/howto/regex.html#regex-howto) and [here](https://docs.python.org/3.6/library/re.html#re-syntax).

## Raw Strings

When writing regular expressions in Python as string literals, you should put an `r` before your string literal, so you can more easily write and read backslashes.

```python
s1 = 'we can\'t write \\ as easily, but escapes \' work'
s2 = r'we can write \ more easily, but escapes \" dont work'
print(s1) # we can't write \ as easily, but escapes ' work
print(s2) # we can write \ more easily but escapes \" dont work
```


## Matching and Searching

`match` and `search` both use a regular expression to find occurrences of a pattern in a string. The difference between them is that `match` only checks for a match at the beginning of a string, while `search` searches the entire string.

```python
import re
re.match("c", "abcdef")    # no match
re.search("c", "abcdef")   # match
re.search("^c", "abcdef")  # no match
re.search("^a", "abcdef")  # match
```

If the pattern isn't found, the result will be `None`, allowing us to use these functions in an `if` clause.

```python
import re
regex = r"([a-zA-Z]+) (\d+)"
if re.search(regex, "June 24"):
    ...
```

We can also use `match` and `search` to find the location and text that was matched.

- `start` returns the start of the match
- `end` returns the end of the match
- `group()` and `group(0)` return the full match
- `group(1)`, `group(2)`, etc return the capture groups in order from left to right


```python
import re
regex = r"([a-zA-Z]+) (\d+)"
match = re.search(regex, "June 14")

print(match.start()) # the beginning of the match, 0
print(match.end()) # the end of the match, 7

print(match.group()) # same as match.group(0), 'June 14'
print(match.group(1)) # 'June'
print(match.group(2)) # '24'
```

```python
import re
m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
m.group(0)     # The entire match 'Isaac Newton'
m.group(1)     # The first parenthesized subgroup 'Isaac'
m.group(2)     # The second parenthesized subgroup 'Newton'
m.group(1, 2)  # Multiple arguments give us a tuple ('Isaac', 'Newton')
```

## Splitting

`split` works just like it does with strings, but allows for regular expressions rather than splitting on a particular string.

```python
import re
s = "this isn\'t the best. test? and I think, this may work! yay."
print(re.split('[.?!]', s))
```

## Compiling Regular Expressions

`compile` allows us to 'compile' a regular expression, this allows us to use special syntax when defining the regex, and allows us to re-use a regex without re-writing it.

```python
import re
reg_exp = re.compile(r'Hello, (\w+)', re.I)
match = reg_exp.search('Why hello, Alice.')
# find the position of the first match
match.start()  # 4
```





