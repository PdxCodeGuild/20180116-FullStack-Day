
# HTML Elements

Many of these come with default styling from the browser. However all can be altered using CSS, thus their meaning is largely what you give to them. For a complete list of tags, look [here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element) and [here](https://www.w3schools.com/tags/).


## Overview

### Common Elements

| element | description |
|---  |---    |
| [h1, h2, etc](#header-tags) | headers |
| [p](#paragraph-tags) | paragraph |
| [q](#quotes-and-block-quotes) | quote |
| [blockquote](#quotes-and-block-quotes) | block quote |
| [pre](#pre-formatted-text) | pre-formatted text |
| [hr](#lines-and-breaks) | horizontal line |
| [br](#lines-and-breaks) | line break |
| [a](#anchor-tags) | link, uses attribute `href` |
| [img](#image-tags) | image, uses attributes `src`, ` |
| [div](#division-tags) | division, block element, used to organize elements |
| [span](#span-tags) | span, inline element, used to organize elements |
| [table, tr, td, th](#tables) | table, row, column, header |
| [ol, ul, li](#ordered-and-unordered-lists) | ordered list, unordered list, list item |


### Interactive Elements

| element | description |
|---  |---    |
| [buttons](#button) | button |
| [input](#input) | various forms of input, uses attribute `type` |
| [select, option](#dropdown-lists) | drop-down list |

### Text Formatting Elements

| element | description |
|---  |---    |
| [b](#text-formatting-elements) | bold text |
| [strong](#text-formatting-elements) | important text, usually bold |
| [i](#text-formatting-elements) | italic text |
| [em](#text-formatting-elements) | emphasized text, usually italic |
| [mark](#text-formatting-elements) | marked or highlighted text |
| [small](#text-formatting-elements) | small text |
| [del](#text-formatting-elements) | deleted text (line-through) |
| [ins](#text-formatting-elements) | inserted text (underlined) |
| [sub](#text-formatting-elements) | subscript text |
| [sup](#text-formatting-elements) | superscript text |
| [time](#text-formatting-elements) | identify a time "11:23" within text |


### Semantic Elements

| element | description |
|---  |---    |
| article | an article |
| aside | for content set aside (a sidebar) |
| details | additional details the user can show or hide |
| figure | a figure |
| figcaption | the caption for a figure |
| footer | the footer of a page |
| header | the header of a page |
| main | the main content of a page
| nav | a set of navigation links |
| section | a section of a page |
| summary | a summary |


### Common Attributes

| attribute | description |
|--- |--- |
| id | a unique identifier |
| style | inline css |
| class | css class |
| name | used when submitting data from a form |
| title | tool-tip, text that's displayed on mouse hover |
| src | source - used on `img` and `script` tags |
| href | reference - used on `a` and `link` tags |
| alt | used in `img` tags to display text when loading the image fails |
| width, height | used on `img` and `canvas` tags |


## Common Elements

### Header Tags

The header (`h1`, `h2`, etc) let us define titles.

```html
<h1>This is ordinarily used for the title</h1>
<h2>This is a chapter title</h2>
<h3>This is a sub-chapter title</h3>
<h4>and so on...</h4>
<h5>and so on...</h5>
```

### Paragraph Tags

The paragraph `p` tag lets us define paragraphs

```html
<p>Lorem ipsum dolor sit amet, consectetur...</p>
<p>Suspendisse elementum enim sed consectetur...</p>
<p>Donec at ligula hendrerit....</p>
```

### Quotes and Block-Quotes

```html
<q>this is a quote</q>

<blockquote>This is a blockquote. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam consectetur nisi nec orci maximus, at facilisis lorem dignissim. Fusce vitae orci pharetra, facilisis dui ut, ullamcorper ex.</blockquote>
```

### Pre-formatted Text

The `<pre>` tag allows pre-formatted text, and preserves spaces and line breaks.

```html
<pre>
  My Bonnie lies over the ocean.

  My Bonnie lies over the sea.

  My Bonnie lies over the ocean.

  Oh, bring back my Bonnie to me.
</pre>
```

### Lines and Breaks

The two tags `<hr/>` and `<br/>` are used without closing tags, and represent a broad horizontal line and line break respectively.

### Anchor Tags

The anchor tag `a` lets us create links.

```html
<a href="http://www.google.com">click this</a>
```

You can also create "internal links", which will take you do another part of the page. This is commonly done to make a table of contents. Note how the `href` begins with a `#` and takes us to the element with the matching `id`.

```html
<a href="#myheading">go to My Heading</a>
<h2 id="myheading">My Heading</h2>
```


### Image Tags

An `img` tag lets us display an image. The `src` attribute can be a relative path or a url. The `alt` is the text that will be displayed if the image fails to load.

```html
<img src="http://www.ackermanplumbing.com/ackermanplumbingserviceslogo.png" alt="Ackerman Plumbing" width="50" height="50"/>
```



### Division Tags

The `div` tag represents a generic block-level container.

```html
<div>This is a generic division</div>
```


### Span Tags

The `span` tag represents a generic inline-level container.

```html
<span>This is a generic span</span>
```


### Tables

Table are defined first by row, then by column.

```html
<table>
    <tr>
        <td>A</td>
        <td>B</td>
    </tr>
    <tr>
        <td>C</td>
        <td>D</td>
    </tr>
    <tr>
        <td>E</td>
        <td>F</td>
    </tr>
</table>
```

Tables can also contain a top row of `th` 'table head' tags:

```html
<table>
 <tr>
   <th>Month</th>
   <th>Savings</th>
 </tr>
 <tr>
   <td>January</td>
   <td>$100</td>
 </tr>
</table>
```



### Ordered and Unordered Lists

Unordered lists are shown with bullet points, ordered lists are shown with numbers.

```html
<ul>
    <li>Apple</li>
    <li>Banananana</li>
    <li>Pear</li>
</ul>

<ol>
    <li>Apple</li>
    <li>Banananana</li>
    <li>Pear</li>
</ol>
```


## Interactive Elements

### Buttons

```html
<button>this is a button</button>
```

### Input

`input` tags allow for user-input.

```html
<input type="text"/>
<input type="date"/>
<input type="color"/>
<input type="password"/>
<input type="radio"/>
<input type="checkbox"/>
```

If radio buttons are given the same `name` attribute, only allow one among them can be selected at any time.

```html
<input type="radio" name="gender" value="male"> Male<br>
<input type="radio" name="gender" value="female"> Female<br>
<input type="radio" name="gender" value="other"> Other
```

### Dropdown Lists

A `select` tag defines a dropdown list. Each `option` defines an option of that dropdown list. Note that the `value` attribute differs from the inner text. The inner text servers human interests, the `value` serves the code's interests.

```html
<select>
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <option value="mercedes">Mercedes</option>
  <option value="audi">Audi</option>
</select>
```



## Text Formatting Elements

You can read more about text formatting elements [here](https://www.w3schools.com/html/html_formatting.asp).

| element | description |
|---  |---    |
| b | bold text |
| strong | important text, usually bold |
| i | italic text |
| em | emphasized text, usually italic |
| mark | marked or highlighted text |
| small | small text |
| del | deleted text (line-through) |
| ins | inserted text (underlined) |
| sub | subscript text |
| sup | superscript text |
| time | identify a time "11:23" within text |

```html
<p>Text formatting elements are meant to be embedded within text and determine how the text is rendered. They allow you to create <b>bold text</b> and <strong>strong text</strong>, <i>italic</i> and <em>emphasized</em> text, <mark>marked</mark>, <small>small</small>, <del>deleted</del>, <ins>inserted</ins>, <sub>subscript</sub>, <sup>superscript</sup>, and time <time>11:23</time>.</p>
```

## Semantic Elements

You can read more about semantic elements [here](https://www.w3schools.com/html/html5_semantic_elements.asp).



