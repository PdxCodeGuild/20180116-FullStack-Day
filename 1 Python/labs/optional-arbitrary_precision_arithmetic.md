
# Lab: Arbitrary Precision Arithmetic

[Arbitrary Precision Arithmetic](https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic) is a way of performing arithmetic with greater precision than that offered by ordinary ints and floats. One python library for this is [mpmath](http://mpmath.org/).

## Addition

Remember doing [long addition](https://en.wikipedia.org/wiki/Elementary_arithmetic#Example) in elementary school? You could represent an 'big int' as a list of ints. To add them, loop over the digits from 'right' to 'left', keeping track of the 'carry'. Also be wary of numbers with differing number of digits. Prompt the user for each number and print out their sum.

```
What is the first number? 23422340923410340239482304
What is the second number? 303003025050020203492
23422340923410340239482304 + 303003025050020203492 = 23422643926435390259685796
```


## Multiplication

A simple (but inefficient) way of implementing multiplication is through repeated addition. For example, 564*6 = 564+564+564+564+564+564. A more efficient way would be [long multiplication](http://mathworld.wolfram.com/LongMultiplication.html).