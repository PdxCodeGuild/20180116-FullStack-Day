
# Python and JavaScript

In Python `if`, `while` and `for` don't require parentheses, have colons, and use indentation to define the body. In JavaScript, these statements **do** require parentheses, don't have a colon, and require curly braces to define the body. If you don't write curly braces, the next statement will be considered the body.

| Python | JavaScript |
|--- |--- |
| True False | true false |
| and | && |
| or | &#124;&#124; |
| not | ! |
| None | null |
| self | this |
| if c: | if (c) {} |
| elif c: | else if (c) {} |
| else: | else {} |
| while c: | while (c) {} | 
| for i in range(len(mylist)): | for (let i=0; i<myarray.length; ++i) {} |


## If Statements

```python
temperature = int(input('what is the temperature?'))
if temperature >= 80:
    print('hot')
elif temperature >= 70:
    print('warm')
elif temperature >= 60:
    print('chilly')
else:
    print('cold') 
```


```javascript
let temperature = prompt('what is the temperature?');
if (temperature >= 80) {
    alert('hot');
} else if (temperature >= 70) {
    alert('warm');
} else if (temperature >= 60) {
    alert('chilly');
} else {
    alert('cold');
}
```



## While Loops

In Python, `while` loops don't need parentheses and use a colon and indentation.

```python
i = 0
while i < 10:
    print(i)
    i += 1
```

In JavaScript `while` loops need parentheses and use curly braces.

```javascript
let i = 0;
while (i < 10) {
    console.log(i);
    i += 1;
}
```

## For Loops

In Python, `for` loops are structured very differently:

```python
for i in range(10):
    print(i)
```

The three parts of a JavaScript for loop are the **initialization**, **condition**, and **increment**.

```javascript
for (let i=0; i<10; ++i) {
    console.log(i);
}
```


## Modulus

Modulus works differently in each language for negative numbers.

#### Modulus in Python

```python
for i in range(-4, 5):
    print(f'{i}%3={i%3}')
```
```
-4%3=2
-3%3=0
-2%3=1
-1%3=2
0%3=0
1%3=1
2%3=2
3%3=0
4%3=1
```

#### Modulus in JavaScript

```javascript
for (let i=-4; i<5; ++i) {
    console.log(i+'%3='+(i%3));
}
```

```
-4%3=-1
-3%3=0
-2%3=-2
-1%3=-1
0%3=0
1%3=1
2%3=2
3%3=0
4%3=1
```
