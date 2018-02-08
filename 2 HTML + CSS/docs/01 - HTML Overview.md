
# HTML Overview

[HTML](https://en.wikipedia.org/wiki/HTML) stands for 'hypertext markup language', hypertext meaning that it also contains multimedia such as images, sound, and video, markup language meaning it's for formatting. HTML is the skeleton of a page, forming its fundamental structure. HTML is displayed, not 'run' like Python. You can read more about HTML on the [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML) or [w3schools](https://www.w3schools.com/html/default.asp).

HTML5 is the latest standard of HTML, and includes support for canvas and video elements, semantic elements, and much more. All modern browsers support HTML5, but some older browsers may not. Certain businesses are limited to older browsers, so you may need to write code that's compatible with them. You can view browser compatibility [here](https://html5test.com/results/desktop.html).

The [DOM](https://en.wikipedia.org/wiki/Document_Object_Model) (Document Object Model) represents the hierarchical structure of [elements](https://en.wikipedia.org/wiki/HTML_element) that make up an HTML document.



## HTML Syntax

HTML elements (or 'tags') have three parts- the **element name**, **attributes** and **inner HTML** or **inner text**. Elements that contain other elements are called 'parents', elements contained in other elements are called 'children'. In general you should **use double quotes for attributes, and use lowercase for element names and attributes**.


```html
<element attribute="value">inner text</element>
<element attribute1="value1" attribute2="value2">
    <innerelement></innerelement>
</element>
```

## Void Elements

Void or empty elements do not have closing tags, and including closing tags will produce an error. The slash at the end is optional, but it's more explicit to include it (otherwise it looks like an open tag with no closing tag). Common void elements include `br`, `hr`, `img`, `input`, `link`, and `meta`. You can view a full list [here](https://developer.mozilla.org/en-US/docs/Glossary/Empty_element). 

```html
<input type="text" value="ok"/>
<input type="text" value="also ok">
```


## Page Template

Below is general form of an HTML document.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Demo Page</title>
  </head>
  <body>
    <p>Hello world!</p>
  </body>
</html>
```

- The `DOCTYPE` tag tells the browser that the document contains HTML. If omitted, some browsers will revert [quirks mode](https://en.wikipedia.org/wiki/Quirks_mode) for rendering.
- The `html` tag contains the entire document
- The `head` tag contains metadata, nothing inside of it is rendered in the page.
    - The `title` tag contains the text that's displayed in the browser tab, or the top of the browser window. It should contain the site name and a page name.
- The `body` tag contains the document's content, what will be shown to the user
- the `p` tag represents a paragraph


## Meta Tags

```html
<meta name="author" content="Your Name">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

## Comments

Comments in HTML are represented by a special tag, beginning with an explanation point and two hyphens, and ending with two hyphens.

```html
<!-- this is a comment -->
```

## Block and Inline Elements

[Block](https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements) elements will take up the full available width and force other elements to move to a new line. Examples of block elements are `p`, `h1`, `div`, `ol`/`ul`, and `form`.

[Inline](https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements) elements only take the amount of space they need, and allow other elements to exist on the same line. Examples of inline elements are `span`, `img`, and `a`.

## Preprocessors

There are several HTML preprocessors: [Haml](http://haml.info/), [Jade](http://jade-lang.com/), [Slim](http://slim-lang.com/index.html), and [Markdown](https://en.wikipedia.org/wiki/Markdown).

