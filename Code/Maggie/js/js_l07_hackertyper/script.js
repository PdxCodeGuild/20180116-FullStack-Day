//selectors
let textarea = document.querySelector('textarea');
let output = document.querySelector('#new');
let cursor = document.querySelector('#cursor');
cursor.style.opacity = 0;
//setting configuration
textarea.style.display = 'none';
original_text = textarea.value;
let display_text = '';
counter = 0;

// // cursor_char = '▩'
setInterval(function() {blink()}, 200);

function blink() {
	cursor.style.opacity = (cursor.style.opacity == 0)? 1:0;
}

window.onkeypress = function() {
	display_text += original_text[display_text.length].replace(/\n/g, '<br/>');
	output.innerHTML = display_text;
}

