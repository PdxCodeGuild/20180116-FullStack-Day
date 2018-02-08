
# HTML Elements

For a complete list of tags, look [here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element) and [here](https://www.w3schools.com/tags/).


## Common Elements

| element | description |
|---  |---    |
| h1, h2, etc | headers |
| p | paragraph |
| q, blockquote | quote |
| blockquote | block quote |
| hr | horizontal line |
| br | line break |
| a | link, uses attribute `href` |
| img | image, uses attributes `src`, ` |
| pre | pre-formatted text |
| div | division, used to organize elements |
| table, tr, td, th | table, row, column, header |
| ol, ul, li | ordered list, unordered list, list item |
| input | various forms of input, uses attribute `type` |
| select, option | drop-down list |
| button | button |
 


## Common Attributes

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


## Explanations and Examples

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


### Input and Select

`input` tags allow for user-input. A `select` tag defines a drop-down box.

```html
<input type="text"></input>
<input type="date"></input>
<input type="color"></input>
<input type="password"></input>
<input type="radio"></input>
<input type="checkbox"></input>
<select>
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <option value="mercedes">Mercedes</option>
  <option value="audi">Audi</option>
</select>
```

If radio buttons are given the same `name` attribute, they'll only allow one option to be selected at a time.

```html
<input type="radio" name="gender" value="male"> Male<br>
<input type="radio" name="gender" value="female"> Female<br>
<input type="radio" name="gender" value="other"> Other
```

### Buttons

```html
<button>this is a button</button>
```
