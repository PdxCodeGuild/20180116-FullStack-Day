
# Classes

Classes, like functions and modules, are another of the major building-blocks of a python program. They represent the grouping of data and functions which together serve a common purpose.

## Types

Classes also represent types, like those we've experienced before (`int`, `float`, `string`, `list`, etc). We can call the initializers of our built-in types as well, rather than literals as we've been using them. Creating classes allows us to define custom types.

```python
# every object in python has a type
x = 5
print(type(x)) # 'int'
y = 'hello'
print(type(y)) # 'str'
print(type(type(y))) # 'type'
```

## Initializers

The built-in types also have initializers, which allow us to create instances of the type.

```python
# call the initializer of the str class
s = str() # equivalent to: s = ''

# call the initializer of the int class
i = int() # equivalent to: i = 0
```

Our classes can have initializers too, which allows us to create instances of them. The initializer is a special type of function which uses the parameters passed into it to initialize the instance. Here, we copy the parameters `x` and `y` into the instance by assigning them to variables on `self`, which is an object that represents the class' "self".

The variables associated with a class are called 'member variables', 'attributes', or 'fields'. The functions associated with a class are called 'methods'.


```python
class Point:
    def __init__(self, x, y): # this is the initializer
        self.x = x # these are member variables
        self.y = y
    
p = Point(5,2) # call the initializer, instantiate the class
print(p.x) # 5
print(p.y) # 2

print(type(p)) # Point
```

If you tried to do this with dictionaries, every time you'd want to refer to the member variables `x` and `y`, you'd have to write `p['x']` and `p['y']`. If you used lists, you'd have to refer ambiguously to `p[0]` and `p[1]`. You'd also have no way of checking the type, or attaching functions to the object.

```python
import math

# we could instead use dictionaries instead of classes
#p1 = {'x': 5, 'y': 2}
#p1['x']

# or just use lists, and write functions to perform operations on those lists
def distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return math.sqrt(dx*dx + dy*dy)

p1 = [5, 2]
p2 = [8, 4]
print(distance(p1, p2))
```


## Methods

Classes allow us to write 'methods' or 'member-functions', which are functions that are called 'on the object'. These are exactly like regular functions, except that the first parameter is always 'self'.

```python
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def distance(self, p): # method, or 'member function'
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)
    
    def scale(self, v):
        self.x *= v
        self.y *= v
    
p3 = Point()
p1 = Point(5,2)
p2 = Point(8,4)
dist = p1.distance(p2) # or p2.distance(p1), either works
print(dist)

# similar to how we can call methods of the str class
s = 'hello world'
print(s.split(' '))
```

## Static Variables

## Static Methods

Static methods are methods that belong to the **type** and **not** the instance. They're represented by an `@staticmethod` above the function declaration.


```python
import math

class Point:
    ...
    
    @staticmethod
    def from_polar(r, theta): # static methods belong to the type, not the instance
        px = r * math.cos(theta)
        py = r * math.sin(theta)
        return Point(px, py)

    
polar_point = Point.from_polar(5.0, math.pi/6)
polar_point.scale(2)
```



## Private Variables

We can specify private variables to maximize **encapsulation**. What if the variable is sometimes in an 'invalid' state, or other variables depend on its value, or setting its value directly could have strange side-effects. There are many situations where a class' variable should not be accessible from the outside. A variable is made private by placing two underscores before the variable name.

```python
import math

class PointPriv:
    def __init__(self, x, y):
        self.__x = x  # use two underscores to denote a private variable
        self.__y = y
    
    def distance(self, p):
        dx = self.__x - p.__x # still accessible from inside methods
        dy = self.__y - p.__y # still accessible to other members of the same class
        return math.sqrt(dx*dx + dy*dy)

p1 = PointPriv(5,2)
p2 = PointPriv(7,8)
print(p1.distance(p2))
print(p1.__x) # AttributeError: 'PointPriv' object has no attribute '__x'
```

Note that these variables are still accessible, and are merely re-named when the code is run. Thus it is not an obligation not to access it, only a very strong recommendation.

```python
print(p1.__dict__) # {'_PointPriv__x': 5, '_PointPriv__y': 2}
print(p1._PointPriv__x)   # 5
```

Below is an example where private variables are useful. If other code changed the value of `alpha`, it wouldn't have any effect on the transformation, which they wouldn't expect. So we restrict access to `alpha` but provide a 'setter' method, which ensures the `cos_alpha` and `sin_alpha` terms are properly set.

```python
import math

class Rotator:
    
    def __init__(self, alpha):
        self.setAlpha(alpha)
    
    def set_alpha(self, alpha): #encapsulation
        self.__alpha = alpha
        self.cos_alpha = math.cos(alpha)
        self.sin_alpha = math.sin(alpha)
    
    def rotate(self, px, py):
        rx = px*self.cos_alpha + py*self.sin_alpha
        ry = -px*self.sin_alpha + py*self.cos_alpha
        return rx, ry
```

## Private Methods

Similar to private variables, private methods are denoted with 2 underscores. Private methods are useful if you have a bit of code that's re-used from within your class but you don't want to expose to outside code.


```python
class MyClass:
    
    def __init__(self):
        pass
    
    def __privatemethod(self, x):
        print(x)
    
    def publicmethod(self):
        self.__privatemethod('hi!')

mc = MyClass()
mc.publicmethod() # hi!
mc.__privatemethod() # AttributeError: 'MyClass' object has no attribute '__privatemethod'
```



## Inheritance

Inheritance lets us extend the functionality of a class by adding additional methods and fields. You can visualize it like an onion, with the super-class in the center, and a sub-class representing a new shell. The child class has all the attributes of its parent, but additional attributes all its own.

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Squirrel(Animal): # inherit from Animal
    def __init__(self, name):
        super().__init__(name) # invoke the parent's initializer

s = Squirrel('Clarence')
print(s.name)
```


### Multiple Inheritance

```python
class ParentA:
    def __init__(self):
        super().__init__()
        print('parent a initializer')

class ParentB:
    def __init__(self):
        super().__init__()
        print('parent b initializer')

class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__()

c = Child()
```


```python
class ParentA:
    def __init__(self):
        print('parent a initializer')

class ParentB:
    def __init__(self):
        print('parent b initializer')

class Child(ParentA, ParentB):
    def __init__(self):
        ParentA.__init__(self)
        ParentB.__init__(self)

c = Child()
```


## Dunder Methods

Classes can implement special methods, called 'dunder methods' which are denoted by two underscores. One which we've already seen is `__init__`, which represents the initializer. For more info, check the [official docs](https://docs.python.org/3/reference/datamodel.html#special-method-names).


### Dunder Methods Overview

| method    | equivalent |
| ---       | ---        |
| \_\_str__ | str(a)     |
| \_\_repr__ | repr(a) |
| \_\_eq__  | a == b     |
| \_\_ne__  | a != b     |
| \_\_lt__  | a < b      |
| \_\_le__  | a <= b     |
| \_\_gt__  | a > b      |
| \_\_ge__  | a >= b     |
| \_\_add__ | a + b    |
| \_\_sub__ | a - b     |
| \_\_mul__ | a * b     |
| \_\_truediv__ | a / b     |
| \_\_floordiv__ | a // b     |
| \_\_contains__ | a in b |
| \_\_len__ | len(a)     |
| \_\_getitem__ | a[i]     |
| \_\_iter__ | for a in b (initially) |
| \_\_next__ | for a in b (each iteration |
| \_\_call__ | a() |


### \_\_str__

The most common dunder methods is `__str__`. First consider what happens when you try and print a string. The python interpreter doesn't know how to create a string representation of an instance of the class, so by default it just prints the class name and a memory address.

```python
class Point:
    ...
p = Point(5, 2)
print(p) # <__main__.Point object at 0x04FF48B0>
```

To be able to print a more human-friendly string, we can implement the `__str__` method. This method is invoked by `str(x)` and `print(x)`, so the three `print` statements below print the same thing.

```python
class Point:
    ...
    def __str__(self): # specify a str conversion
        return '['+str(self.x)+','+str(self.y)+']'

p = Point(5, 2)
print(p.__str__()) # [5,2], but don't use it this way
print(str(p)) # [5,2]
print(p) # [5,2]
```


### \_\_repr__

[repr](https://docs.python.org/3/library/functions.html#repr) returns the 'official' representation of a string. This should yield a copy when passed to `eval`.

```python
class Point:
    ...
    def __repr__(self):
        return f'Point({self.x},{self.y})'

p = Point(5, 2)
print(repr(p))
p_copy = eval(repr(p))
```

### \_\_eq__ and \_\_neq__

These two implements allow the comparison of class instances. Note that `is` will work regardless, because it checks if two variables refer to literally the same object.

```python
class Point:
    ...
    def __eq__(self, p):
        return self.x == p.x and self.y == p.y
    
    def __neq__(self, p):
        return self.x != p.x or self.y != p.y

p1 = Point(5, 2)
p2 = Point(5, 2)
p3 = Point(8, 6)
print(p1 == p2) # True
print(p1 == p3) # False
print(p1 != p2) # False
print(p1 != p3) # True
```



### \_\_getitem__ and \_\_len__

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        return None

    def __len__(self):
        return 2

p = Point(5, 2)
for i in range(len(p)):
    print(p[i])
```