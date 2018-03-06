
# CSS Overview

CSS stands for [Cascading Style Sheets](https://en.wikipedia.org/wiki/Cascading_Style_Sheets), "cascading" meaning that style rules are evaluated by priority. That is, if a style rule is applied to a particular element, it'll override the rules applied to its parent. Whereas HTML is the raw skeleton of a page, CSS adds fonts, colors, margins, positioning, animations, and more. You can view a list of CSS libraries and frameworks [here](../../Libraries%20and%20Frameworks.md#css-frameworks).

## CSS Syntax

CSS has two major parts: properties and selectors. Properties set the color, shape, positioning, etc of elements. Selectors determine what HTML elements receive the given properties.

```css
selector {
    property: value;
}
```

You can add comments in CSS with `/* ... */`

```css
/* this is for a very special div,
 * one that requires lots of explanation
 */
div {
    color: #0FA0CE; /* a beautiful color */
}
```


## Priority

CSS Rules will be applied with the following priority (highest first). You can place a special keyword on rules which will automatically give them the highest priority.

```css
div {
    /* overwrite all other rules */
    color: red !important;
}
```

| Priority | Definition |
|--- |--- |
| 1 | rules with `!important` |
| 2 | inline style |
| 3 | media queries |
| 4 | user-defined (through developer panel) |
| 5 | internal and external CSS, by last defined rule |
| 6 | parent element's value |
| 7 | browser default |

## Including CSS

There are three ways to add CSS to a page.

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

You can also keep css in external files. This is useful if you want to use the same CSS across multiple pages. The `link` tag should also go inside the `head`. The `type="text/css"` isn't necessary for HTML5, but it is for HTML4 and below. Be aware that it's **common for your browser to cache external CSS, and you won't see changes you've made until you do a "hard refresh".** You can find out how to do this in various browsers [here](https://en.wikipedia.org/wiki/Wikipedia:Bypass_your_cache).

```html
<link rel="stylesheet" type="text/css" href="mystyle.css"/>
```

You can also include CSS from a remote server by putting a URL in `href`. Your browser will download the CSS when the page is rendered. This is commonly served by a CDN "content delivery network".

```html
<link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
```

## CSS Lengths

You can read more about lengths in CSS [here](https://css-tricks.com/the-lengths-of-css/), [here](https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Values_and_units), and [here](https://www.w3schools.com/cssref/css_units.asp). Keep in mind that in CSS a 'pixel' [isn't the same as a screen pixel](https://stackoverflow.com/questions/27382331/how-a-css-pixel-size-is-calculated).


| Unit | Relative To | Description |
|--- |--- |--- |
| px | absolute | pixels |
| cm | absolute | centimeters |
| mm | absolute | millimeters |
| in | absolute | inches |
| pt | absolute | point, 1pt == 1/72in |
| pc | absolute | pica, 1pc == 12pt |
| em | font | font size of the element, does not change with font family |
| rem | font | font size of root element (html), does not change with font family |
| ex | font | the height of "x", does change with font family |
| ch | font  | the width of "0", does change with font family |
| vw | viewport | 1vw == 1% of the width of the viewport |
| vh | viewport | 1vh == 1% of the height of the viewport |
| vmin | viewport | 1vmin == 1% of the viewport's smaller dimension |
| vmax | viewport | 1vmax == 1% of the viewport's larger dimension |
| %	 | parent | relative to the length of the parent's width or height |


## CSS Colors

RGB is short for [red green blue](https://en.wikipedia.org/wiki/RGB_color_model), with each value going from 0 to 255 (0 to FF in hexidecimal). Hexidecimal RGB values can also be specified with 3 values, in which case the digit is repeated (`#FFF` is the same as `#FFFFFF`).

HSL is short for [hue saturation lightness](https://en.wikipedia.org/wiki/HSL_and_HSV), with hue going from 0 to 360, and saturation and lightness going from 0% to 100%. The A stands for [alpha](https://en.wikipedia.org/wiki/Alpha_compositing), which goes from 0.0 to 1.0. You can learn more about CSS colors at the [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value) and [w3schools](https://www.w3schools.com/cssref/css_colors.asp). You can view a nicely organized list of named colors [here](http://htmlcolorcodes.com/color-names/).

| color type | examples |
|--- |--- |
| RGB Hex | `#7FFFD4`, `#A9A9A9`, `#F00` |
| RGB Decimal | `rgb(127, 255, 212)` |
| RGBA Decimal | `rgba(255, 0, 0, 0.5)` |
| HSL | `hsl(120, 100%, 50%)` |
| HSLA | `hsla(120, 100%, 50%, 0.3)` |
| named color | `red`, `goldenrod`, `magenta` |




## Removing the Browser's Built-In CSS

You can remove the browser's built-in css by including [normalize.css](http://necolas.github.io/normalize.css/) or [reset.css](https://meyerweb.com/eric/tools/css/reset/). You can read about the differences [here](https://stackoverflow.com/questions/6887336/what-is-the-difference-between-normalize-css-and-reset-css).


## CSS Preprocessors

The two most popular CSS preprocessors are [Sass/SCSS](http://sass-lang.com/) and [Less](http://lesscss.org/). For info on using CSS preprocessors in PyCharm, look [here](https://www.jetbrains.com/help/pycharm/compiling-sass-less-and-scss-to-css.html).
