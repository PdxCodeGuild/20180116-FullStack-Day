



let guesses = 0;
let correct = 0;

while (guesses < 10) {

    let guess = prompt('> guess the number?\n> ');
    guesses += 1;

    let x = Math.floor(Math.random() * 10);

    if (guess === x) {
        correct += 1;
        alert('correct');

    } else {
        alert('try again!');
        }
}

alert(`You got ${correct} correct!`);