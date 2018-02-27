// add button - from https://codepen.io/knyttneve/pen/rGLxbP

let plus = document.querySelector('#plus');
let new_todo = document.querySelector('#new_todo');
let new_appt = document.querySelector('#new_appt');
let new_work = document.querySelector('#new_todo');
let new_meet = document.querySelector('#new_work');
let new_play = document.querySelector('#new_play');

function plusToggle() {
    plus.classList.toggle('plus--active');
    }

plus.addEventListener('click', plusToggle);

new_todo.addEventListener('click', function() {
    $('#todo_input').removeClass('hidden-input');
    $('#todo_submit').removeClass('hidden-input');
});