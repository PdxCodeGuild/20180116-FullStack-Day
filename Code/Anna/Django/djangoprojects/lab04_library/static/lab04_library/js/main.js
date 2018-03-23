$(document).ready(function() {
    Materialize.updateTextFields();
    $('select').material_select();
    $('.modal').modal();
});

let register_bt = document.querySelector('#register_bt');
let password_input1 = document.querySelector('#password_input1');
let password_input2 = document.querySelector('#password_input2');
register_bt.onclick = function() {
    if (password_input1.value !== password_input2.value) {
        alert("Your passwords don't match!");
        console.log("Your passwords don't match!");
        return false; // cancels form submission! This or prevent default needed
    }
};