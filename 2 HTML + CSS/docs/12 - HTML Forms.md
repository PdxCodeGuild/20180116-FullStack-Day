
# HTML Forms

Forms are a particular element that allows us to submit data to the back-end. You can read more about forms on the [MDN](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms).

## Input and Select Elements

An `input` element allow for user input, and has a `type` attribute. You can read more about `input` on the [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input).

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

A `select` tag defines a dropdown list. Each `option` defines an option of that dropdown list. Note that the `value` attribute differs from the inner text. The inner text servers human interests, the `value` serves the code's interests. Note that the `name` goes on the `select` and not the `option`.

```html
<select name="car">
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <option value="mercedes">Mercedes</option>
  <option value="audi">Audi</option>
</select>
```

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

## The Placeholder Attribute

You can also add a `placeholder` attribute to show some text in the 'background' of the input field. This text disappears when a value is entered.

```html
<input type="text" name="name" value="jane" placeholder="enter your name"/>
```

## The Disabled Attribute

To disabled an input field, you can add the `disabled` attribute without any parameters. This will prevent the user from entering any value into the input field. It doesn't matter what the value of the attribute is, as long as it's present, the input will be disabled.

```html
<input type="text" name="name" value="jane" disabled/>
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