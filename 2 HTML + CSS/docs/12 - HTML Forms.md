
# HTML Forms

Forms are a particular element that allows us to submit data to the back-end. You can read more about forms on the [MDN](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms).


## Form

The most important attributes of a form are `action`, which is the URL we're submitting the data to, and `method` which is the HTTP method we'll use.

```html
<form action="https://requestb.in/1622li71" method="post">
    <input type="text" name="name" value="jane"/>
    <button type="submit">submit</button>
</form>
```

## Fieldset

If a form has many input fields, you should group them together using a `fieldset`. The `legend` tag indicated the caption for a fieldset.


```html
<form action="..." method="...">
  <fieldset>
    <legend>Personal Info</legend>
    Name: <input type="text" name="name"/><br/>
    Email: <input type="text" name="email"/><br/>
    Date of birth: <input type="text" name="dob"/>
  </fieldset>
  <fieldset>
    <legend>Address</legend>
    Street: <input type="text" name="street"/><br/>
    City: <input type="text" name="city"/><br/>
    State: <input type="text" name="state"/>
  </fieldset>
  <button type="submit">submit</button>
</form>
```


## The Required Attribute

You can place the attribute `required` with no value to prevent the form from being submitted without that field being filled. Like `disabled`, the attribute doesn't need a value.


```html
<input type="text" name="name" required/>
```


## The Pattern Attribute

HTML5 brought the `pattern` attribute, which enables you to do validation entirely within HTML. You only have to enter a regular expression into the `pattern` attribute. If the user tries to submit the form and the given input doesn't match the pattern, a message will pop up containing the text in the `title` attribute.

```html
<form action="..." method="...">
    <input type="text" pattern="[a-z]{1,15}" title="username must be between 1 and 15 characters, all lowercase" required/>
    <button type="submit">submit</button>
</form>
```