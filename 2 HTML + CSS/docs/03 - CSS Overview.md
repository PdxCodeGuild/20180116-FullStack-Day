
# CSS Overview

## CSS Syntax

CSS has two major parts: properties and selectors. Properties set the color, shape, positioning, etc of elements. Selectors determine what HTML elements receive the given properties.

```css
selector {
    property: value;
}
```

## Including CSS

There are three ways to add CSS to a page. They'll be applied with the following priority.

1. inline style
2. external and internal style sheets
3. the browser's default style

### Inline CSS

The simplest and quickest way to write CSS is inside a HTML tag's `style` attribute. CSS properties are separated via semi-colons.

```html
<div style="color:blue;background-color:DarkOliveGreen">This is some ugly text</div>
```

Inline styles are fine when experimenting, but consider the following case.

```html
<ol>
    <li style="color:red">Apple</li>
    <li style="color:red">Banananana</li>
    <li style="color:red">Pear</li>
</ol>
```

This can become tedious to work with, because we have to edit the same value in multiple places. Therefore, it's generally better to use a style tag.

### Style Tag

CSS can be placed within its own tag, usually inside the document's `head`. This way your CSS is not tied to any particular element and is all in one place. This makes your code more organized and manageable. The `type` attribute isn't necessary for HTML5, but it is for HTML4 and below.

```html
<html>
    <head>
        <style type="text/css">
            li {
                color:red;
            }
        </style>
    </head>
    <body>
        <ol>
            <li>Apple</li>
            <li>Banananana</li>
            <li>Pear</li>
        </ol>
    </body>
</html>
```

### External CSS

You can also keep css in external files. This is useful if you want to use the same CSS across multiple pages. The `link` tag should also go inside the `head`. The `type="text/css"` isn't necessary for HTML5, but it is for HTML4 and below.

```html
<link rel="stylesheet" type="text/css" href="mystyle.css"/>
```

## CSS Comments

You can add comments in CSS with `/* ... */`


## CSS Preprocessors

The two most popular CSS preprocessors are [Sass/SCSS](http://sass-lang.com/) and [Less](http://lesscss.org/). For info on using CSS preprocessors in PyCharm, look [here](https://www.jetbrains.com/help/pycharm/compiling-sass-less-and-scss-to-css.html).
