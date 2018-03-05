
# JavaScript Overview

## Intro

JavaScript is a front-end language, written in `<script>` tags or in external `.js` files, and run by an interpreter in the browser. You can find more info in JavaScript [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) and [here](https://www.w3schools.com/js/default.asp). You can view a list of JavaScript frameworks [here](../../Libraries%20and%20Frameworks.md#javascript-frameworks).

JavaScript has become the de-factor standrard for front-end. There used to be Flash (which had a JavaScript-like language called ActionScript), Java Applets, and Microsoft's Silverlight. But with the development of stronger standards for JavaScript and the discovery of security holes in the other frameworks, browsers began dropping support.

JavaScript is part of the 'C Family' of languages, those with syntax based on that of C: C++, Java, C#, Objective-C, Swift, Go, and [more](https://en.wikipedia.org/wiki/List_of_C-family_programming_languages). You can find a brief account of the history of C Family languages [here](https://softwareengineering.stackexchange.com/questions/135544/why-are-several-popular-programming-languages-influenced-by-c). Familiarizing yourself with JavaScript syntax will enable you to more easily transition to these languages. That said, a thorough understanding of the principles underlying any one language will enable you to transition to any others. In JavaScript, most of the forms familiar to Python are there: numbers, strings, loops, classes, etc.

JavaScript (as its name implies) is a **scripting** language, meaning it was designed to be quick to write and ad-hoc. This worked well when pages were simple, but as web applications became more complex, its loose syntax became more of a hindrance. It is much easier to write messy code which is difficult to read, debug, and extend. Therefore it's important to impose upon yourself strict organization and 'best practices'.

The latest iteration of the JavaScript specification (called ECMAScript) is ECMAScript 6. All major browsers support ES6, but older browsers might not. You can view a table of features and browse compatibility [here](https://kangax.github.io/compat-table/es6/).


## The Script Tag

In an HTML page, we can specify blocks of JavaScript code using `<script>` tags. You can put these anywhere, but most often you'll put them in the `<head>` or at the bottom of the `<body>`. You may see a `type="text/javascript"` attribute on script tags. This was necessary in HTML4.01, but not in HTML5.

```html
<html>
    <head>
        <script>
            alert('put your code here');
        </script>
    </head>
    <body>
        ...
        <script>
            alert('or here');
        </script>
    </body>
</html>
```

If you put in the head, you cannot do `document.getElementById`, `document.querySelector`, etc, on the elements in the body, because the JavaScript would be executed before the body is loaded. You have to either wrap it in a `window.onload = function () {...}` or put it at the bottom of the body.

A script tag may also reference an external file containing JavaScript, denoted with a `.js` suffix.

```html
<script src="myscript.js"></script>
```

JavaScript can also be written in-line.

```html
<button onclick="alert('Hello World!');">click me</button>
```


## JavaScript Preprocessors

There are various JavaScript preprocessors that make writing JavaScript easier: [CoffeeScript](http://coffeescript.org/), [Babel](https://babeljs.io/), [Typescript](https://www.typescriptlang.org/), [Livescript](http://livescript.net/)

