
# Markdown

Markdown is a simple way to write formatted text in a plain text document. Markdown can be translated directly into HTML. Check out this [cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

## Headings

```markdown
# Heading 1
## Heading 2
### Heading 3
```

```html
<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
```



## Formatted Text



```markdown
*italic*
**bold**
***italic and bold***
~~strike-through~~
```

```html
<i>italic</i>
<b>bold</b>
<i><b>italic and bold</b></i>
<del>strike-through</del>
```


## Unordered Lists

Unordered lists use `*`, `+` or `-`.

```markdown
- alpha
- beta
    - beta1
    - beta2
- gamma
```

```html
<ul>
    <li>alpha</li>
    <li>beta
        <ul>
            <li>beta1</li>
            <li>beta2</li>
        </ul>
    </li>
    <li>gamma</li>
</ul>
```

## Ordered Lists

Ordered lists use numbers, but they needn't be in order.

```markdown
1. alpha
1. beta
    1. beta1
    1. beta2
1. gamma
```

```html
<ol>
    <li>alpha</li>
    <li>beta
        <ol>
            <li>beta1</li>
            <li>beta2</li>
        </ol>
    </li>
    <li>gamma</li>
</ol>
```

## Horizontal Rules

To make horizontal rules, write 3 or more hyphens, asterisks, or underscores.

```markdown
---
***
___
```

```html
<hr/>
<hr/>
<hr/>
```

## Block Quotes

```markdown
> this is a block-quote
```

```html
<blockquote>this is a block-quote</blockquote>
```
