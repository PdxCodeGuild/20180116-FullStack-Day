
# Docstrings

Docstrings are used to provide documentation of source code. Docstrings help those reading the code to better understand what each part means.

Docstrings are defined by triple-quoted strings, you can use single- or double-quoted strings. Check out [PEP 257](https://www.python.org/dev/peps/pep-0257/) for docstring conventions. Docstrings always immediately follow the part of code to which they pretain.

```python
"""this is the module's docstring"""

x = 5
"""this is a variable's docstring"""

def add(a, b):
    """this is a function's docstring"""
    return a + b

class MyClass(object):
    """this is the class's docstring"""

    def my_method(self):
        """this is the method's docstring"""
```

**Variable** docstrings should describe what the variable represents and how it should be used.

**Module** docstrings should start at the very top of the file, and should list all variables, functions, and classes within the module, with a brief summary for each.

**Package** docstrings (`__init__.py`) should contain a list of modules contained in it.

**Function** and **method** docstrings should provide a brief explanation of what operation the function performs. It should list all the parameters and what each parameter represents. It should also describe what it returns.

**Class** docstrings should describe what the class represents and list all attributes and methods of the class. 


### Example

```python
"""
just a test module for demonstrating classes and docstrings
"""

import math


class Point:
    """
    a 2D point with floats
    """

    def __init__(self, x, y):
        """
        point initializer
        :param x: the x value of the point
        :param y: the y value of the point
        """
        self.x = x
        self.y = y

    def distance(self, p):  # method, or 'member function'
        """
        calculate the distance between two points
        :param p: the point to which we'll calculate the distance
        :return: the distance between the two points
        """
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx * dx + dy * dy)

    def scale(self, v):
        """
        scales a point
        :param v: the value to scale by
        :return: nothing
        """
        self.x *= v
        self.y *= v

    def __str__(self):
        """
        :return: the human-readable string representation of this object 
        """
        return f'[{self.x},{self.y}]'


def add(a, b):
    """
    adds two numbers and returns the result
    :param a: the first number to be added
    :param b: the second number to be added
    :return: the sum of the first and second number
    """

    return a + b

```


### `help()`, `__doc__` and `pydoc`

Docstrings can be used with the built-in function `help()`. Pass whatever python variable, function, module, class, etc, into `help` to see its docstring. You can read more about the help function in the [official docs](https://docs.python.org/3.6/library/functions.html#help). You can then access the docstring using the object's `__doc__` attribute.

```python
help(add)
print(add.__doc__)

import os
help(os)
```

`pydoc` is a documentation-buidling package built into the core python library.
 
 
- View documentation in the terminal:  `python -m pydoc <module name>`

- Generate HTML: `python -m pydoc -w <module name>`

For example, try running `python -m pydoc -w os`. You can read more about pydoc in the [official docs](https://docs.python.org/3.6/library/pydoc.html).

### Doctests

[Doctests](https://docs.python.org/3/library/doctest.html) are a way to embed tests inside the docstring of your module.

```python
"""
a simple module with a single method

>>> add(5,2)
7
>>> add(-1, 3)
2
>>> add(-1, -4)
-5
"""

def add(a, b):
    return a + b
```

You can then run the doctest of this module by executing `python -m doctest -v example.py`. This runs the doctest module `example.py` as an argument. If a doctest is successful, it prints nothing. If a test fails, it'll tell you the expected value and the value it received.

Instead of running the doctest on the command-line, you can have the module run the doctest directly. That way, the doctest is executed whenever the module is run.

```python
"""
>>> add(5,2)
7
>>> add(-1, 3)
2
>>> add(-1, -4)
-5
"""

def add(a, b):
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
```


### Sphinx & Epydoc

[Sphinx](http://www.sphinx-doc.org/en/stable/index.html) is a program which can generate documentation in HTML and PDFs from Python source code. You can find a tutorial [here](http://www.sphinx-doc.org/en/stable/tutorial.html). Sphinx allows for two ways of formatting docstrings: [google-style](http://www.sphinx-doc.org/en/stable/ext/example_google.html) and [numpy-style](http://www.sphinx-doc.org/en/stable/ext/example_numpy.html#example-numpy).

[Epydoc](http://epydoc.sourceforge.net/) is another documentation-generator. It uses [Epytext](http://epydoc.sourceforge.net/epytextintro.html) which is a simple markup language for formatting docstring text.
