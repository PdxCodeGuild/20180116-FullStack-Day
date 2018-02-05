
# Practice Problems: Lists



For each practice problem, write a function that returns a value (not just prints it). You can then call the function a couple times to test it, comment those calls out, and move on to the next problem. An example of this format is given below.

```python
def add(a, b):
    return a + b
#print(add(5, 2))
#print(add(8, 1))
```



## Problem 1

Write a function using random.randint to generate an index, use that index to pick a random element of a list and return it.

```
def random_element(a):
    ...

fruits = ['apples', 'bananas', 'pears']
random_element(fruits) could return 'apples', 'bananas' or 'pears'
```

## Problem 2

Write a REPL which asks users for a list of numbers, which they enter, until they say 'done'. Then print out the list.

```
Enter a number (or 'done'): 5
Enter a number (or 'done'): 34
Enter a number (or 'done'): 515
Enter a number (or 'done'): done
[5, 34, 515]
```


## Problem 3

Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.

```python
eveneven([5, 6, 2]) → True
eveneven([5, 5, 2]) → False
```


## Problem 4

Print out every other element of a list, first using a while loop, then using a for loop.

```
>>> nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> print_every_other(nums)
0, 2, 4, 6, 8
```

## Problem 5
Write a function that returns the reverse of a list.

`def reverse(nums):`

## Problem 6
Write a function to move all the elements of a list with value less than 10 to a new list and return it.

`def extract_less_than_ten(nums):`

## Problem 7
Write a function to find all common elements between two lists.

`def common_elements(nums1, nums2):`


## Problem 8
Write a function to combine two lists of equal length into one, alternating elements.

```python
def combine(nums1, nums2):
    ...
combine(['a','b','c'],[1,2,3]) → ['a', 1, 'b', 2, 'c', 3]
```


## Problem 9

Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number

```python
nums = [5, 6, 2, 3]
target = 7
find_pair(nums, target) → [5, 2]
```

Optional: return a list of all pairs of numbers that sum to a target value.


## Problem 10

Write a function that merges two lists into a single list, where each element of the output list is a list containing two elements, one from each of the input lists.

```python
merge([5,2,1], [6,8,2]) → [[5,6],[2,8],[1,2]]
```


## Problem 11

Write a function `combine_all` that takes a list of lists, and returns a list containing each element from each of the lists.

```python
nums = [[5,2,3],[4,5,1],[7,6,3]]
combine_all(nums) → [5,2,3,4,5,1,7,6,3]
```


## Problem 12

Write a function that takes `n` as a parameter, and returns a list containing the first `n` [Fibonacci Numbers](https://en.wikipedia.org/wiki/Fibonacci_number).

```python
fibonacci(8) → [1, 1, 2, 3, 5, 8, 13, 21]
```

## Problem 13

Write functions to find the minimum, maximum, mean, and (optionally) mode of a list of numbers.

```python
def minimum(nums):
    ...

def maxmimum(nums):
    ...

def mean(nums):
    ...

def mode(nums): # (OPTIONAL)
    ...
```


## Problem 14

Write a function which takes a list as a parameter and returns a new list with any duplicates removed.

```python
def find_unique(nums):
    ...
nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
unique_nums = find_unique(nums) → [12, 24, 35, 88, 120, 155]
```