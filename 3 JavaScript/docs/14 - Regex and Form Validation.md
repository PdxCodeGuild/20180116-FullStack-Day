
# Form Validation

There are two ways of doing form validation. You can either use [HTML5's pattern attribute](../../2%20HTML%20+%20CSS/docs/12%20-%20HTML%20Forms.md#the-pattern-attribute), or you can use JavaScript. While the `pattern` attribute is quick and easy, JavaScript gives you more control. You can read more about regex in JavaScript on the [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions).

It's important to note that regular expressions are _not_ a standardized language. Each implementing language does them slightly differently. Regular expressions in JS are slightly different than those in Python. To write them out in JS, use a regexp literal, which is the pattern surrounded by forward slashes `/`.


```js
let regex = /hello, (\w+)/i;
// The result is like an array, but has properties "index" and "input"
let match = regex.exec('Why hello, Alice.');
// The position in the search string of the match.
alert(match.index);  // 4
// Captures starting at 1. 0 is the whole string matched.
alert(match[1]);  // 'Alice'
```

Below is an example using input fields.

```html
<input id="username_input" type="text"/>
<span id='username_info' style="display:none;color:red;">username must be between 1 and 15 lowercase characters</span>
<script>
    let username_input = document.querySelector('#username_input');
    let username_info = document.querySelector('#username_info');
    
    // this event is triggered whenever the value in the input field is changed
    username_input.oninput = function() {
        
      // define a regex pattern
      let pattern = /^[a-z]{1,15}$/;
      
      // if the pattern doesn't the input value, indicate the error
      if (!pattern.test(this.value)) {
        this.style.outline = '1px solid red';
        username_info.style.display = 'inline';
      } else {
        this.style.outline = '1px solid black';
        username_info.style.display = 'none';
      }
    }
</script>
```