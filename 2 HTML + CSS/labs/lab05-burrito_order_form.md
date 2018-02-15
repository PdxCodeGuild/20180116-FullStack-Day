

# Lab 5: Burrito Order Form

Create a burrito order form with the following input controls. Try to incorporate some images and semantic elements. Below are some recommended fields, feel free to use your own. You should include all elements in a `form`, and use `fieldset`s. You may draw some inspiration from [this image](burrito-order-form.png).

Tortilla (radio buttons)
- White Flour
- Wheat Flour
- Spinach
- Corn

Rice (radio buttons)
- White Rice
- Brown Rice

Beans (radio buttons)
- Black Beans
- Pinto Beans

Protein (radio buttons)
- Carnitas
- Chicken
- Sofritas
- None

Additional Ingredients (check boxes)
- Cheese
- Sour Cream

For personal info, use the `required`, `pattern` and `title` attributes of the input fields to verify that the information the user entered is legitimate.

Personal Info
- Username (at least 6 characters)
- Password (at least 6 characters)
- Name (First and Last) (two words, at lease 3 characters each)
- Email Address (one or more numbers/letters, @, one or more numbers/letters, ., one or more numbers/letters)
- Phone Number: (e.g. 293-213-5555)
- Date of Birth: (e.g. 2/13/2627)
- Social Security Number: (e.g. 415-25-2627)
- Street (e.g. 123 Mulberry Ln)
- City, State, Zip (e.g. Portland, OR, 97201)

Once you have your page together, add the attributes `action="https://requestb.in/u96nubu9"` and `method="post"` to your form. Then fill out your form and submit the data. You should see an "ok" response. You can then go [here](https://requestb.in/u96nubu9?inspect) and look at the request's body. Make sure all the relevant data is present to ensure your form is working.