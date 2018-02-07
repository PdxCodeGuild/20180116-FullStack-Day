
# Practice 4: Dictionaries

For each practice problem, write a function that returns a value (not just prints it). You can then call the function a couple times to test it, comment those calls out, and move on to the next problem. An example of this format is given below.

```python
def add(a, b):
    return a + b
#print(add(5, 2))
#print(add(8, 1))
```


## Problem 1

Given a the two lists below, combine them into a dictionary.

```python
def combine(a, b):
    ...
fruits = ['apple', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]
combine(fruits, prices) -> {'apple':1.2, 'banana':3.3, 'pear':2.1}
```


## Problem 2

Using the result from the previous problem, iterate through the dictionary and calculate the average price of an item.

```python
def average(d):
    ...
combined = {'apple':1.2, 'banana':3.3, 'pear':2.1}
average(combined) -> 2.2
```

## Problem 3

Average numbers whose keys start with the same letter. Output a dictionary containing those letters as keys and the averages.

```python
d = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}
unify(d) -> {'a':3, 'b':4, 'c':5}
```
