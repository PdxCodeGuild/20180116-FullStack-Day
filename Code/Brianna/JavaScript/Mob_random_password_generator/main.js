

// TODO: allow for large passwords


let password_length_input = document.querySelector('#password_length_input');
let lower_case_cb = document.querySelector('#lower_case_cb');
let upper_case_cb = document.querySelector('#upper_case_cb');
let numbers_cb = document.querySelector('#numbers_cb');
let specials_cb = document.querySelector('#specials_cb');
let generate_bt = document.querySelector('#generate_bt');
let overlay = document.querySelector('#overlay');
let messagebox = document.querySelector('#messagebox');
let close_overlay_bt = document.querySelector('#close_overlay_bt');

close_overlay_bt.onclick = function() {
  overlay.style.display = 'none';
};

password_length_input.value = 10;
//making lists
let lower_case_characters = 'abcdefghijklmnopqrstuvwxyz';
let upper_case_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
let number_characters = '12345567890';
let special_characters = '`~!@#$%^^&*()_+=-\\/|[]{}<>,.:;';



function show_output(str) {
  messagebox.innerText = str;
  overlay.style.display = 'initial';
}

generate_bt.onclick = function() {
    let master_characters = '';
    if (lower_case_cb.checked) {
    master_characters += lower_case_characters;
    }
    if (upper_case_cb.checked) {
    master_characters += upper_case_characters;
    }
    if (numbers_cb.checked) {
    master_characters += number_characters;
    }
    if (specials_cb.checked) {
    master_characters += special_characters;
    }
    if (master_characters === '') {
    show_output('Your password is \'password123\'');
    return;
    }


  // get the password length
  let password_length = parseInt(password_length_input.value);
  // start with a blank password
  let new_password = '';
  // itterate that number of times
  for (let i=0; i<password_length; ++i) {
    new_password += get_random_character(master_characters);
  }
  // show the new password to the user

  show_output('I have your password! ' + new_password);
};

function get_random_character(str) {
    let random_index = Math.floor(Math.random() * str.length);
    return str[random_index];
}


// check boxes for if we want upper and lower case characters
// Check box for if we want numbers
// check box for special characters yes/no
// button that generates our password
// password emoticon?
// output field for generated password
// three or four different variables that have all the characters in them