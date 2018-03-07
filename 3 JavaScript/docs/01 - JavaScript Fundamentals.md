
# Fundamentals

You can read more about JavaScript syntax on the [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar).

## Declaring Variables

There are three ways to declare variables: `var`, `let` and `const`. The only difference between `var` and `let` is that `let` has a more limited scope. In general, `let` is preferable, unless you your code needs to be compatible with older browsers.

```javascript
if (2 < 10) {
    var x = 10; // scope extends beyond the if
    let y = 11; // scope is limited to the if
}
console.log(x); // 10
console.log(y); // error

for (var x=0; x<10; ++x) {}
alert(x); // 10

for (let y=0; y<10; ++i) {}
alert(y); // error
```

Variables declared `const` cannot change value, this is advantageous for declaring constants.

```javascript
const pi = 3.1415;
pi += 1 // error
```


## Data Types

```javascript
let a = 5; // number
let b = 10.4; // number
let c = "hello!"; // string
let d = true; // boolean
let e = null; // null
let f = undefined; // undefined

// arrays are like python lists
let fruits = ["apple", "bananana", "pear"];
fruits[0] = 'cherry'; // set the element at that position
fruits.push('pomegranate'); // add a new element

// objects are like Python dictionaries
let person = {
    firstName:"John",
    lastName:"Doe",
    age:46
};
person.age += 1;
person['age'] += 1;
```

To convert between types, use `parseInt`, `parseFloat` and `toString`.

```javascript
let x = parseInt('4');
let y = parseFloat('4.2');
let z = x.toString();
```


## Comments

Use `//` for line-comments, `/* ... */` for block-comments.

```javascript
// this is a line comment
let x = 10; // this is another line comment
/* this is a block comment
which can span multiple lines*/
```


## Input

An easy way to get input from a user is `prompt`, a function which takes the text to display as a parameter and returns whatever the user entered.

```javascript
let name = prompt("Please enter your name");
alert("Hello " + name + "! How are you today?");
```

You can also use `input` elements.

```html
<input id="name_input" type="text"/>
<script>
    let name_input = document.querySelector('#name_input');
    let name_value = name_input.value;
    alert(name_value);
</script>
```


## Output

Below are three simple ways of getting output to the user.

The `alert` function shows the user text in the form of a popup.

```javascript
alert('Hello World!');
```

The `console.log` function will print the parameter in the developer console (F12). If the parameter is an object, you'll be able to look through the data much more easily than if it were one giant string.

```javascript
console.log("Hello World!");
```

The `document.write(s)`  function will replace all existing HTML on the page with whatever you give it (which can be a string containing HTML)

```javascript
document.write('<span>Hello World!</span>');
```

