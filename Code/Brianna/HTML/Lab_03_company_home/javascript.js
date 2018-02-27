let today = new Date();
let hourNow = today.getHours();
let greeting;

if(hourNow > 18) {
   greeting = 'Good Evening Bootiers!';
} else if (hourNow > 12) {
    greeting = 'Good Afternoon Bootiers!';
} else if (hourNow > 0) {
    greeting = 'Good Morning Bootiers!';
} else {
    greeting = 'Welcome Bootiers!';
}

document.write('<h3>' + greeting + '</h3>');


