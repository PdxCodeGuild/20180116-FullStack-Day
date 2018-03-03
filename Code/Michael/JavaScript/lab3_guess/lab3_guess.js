

let guess = document.getElementById('guess');
let submit = document.getElementById("submit");

submit.onclick = function () {

    let guesses = 0;
    let correct = 0;

    while (guesses < 10) {
        guesses += 1;
        let x = Math.floor(Math.random() * 10);
        if (guess === x) {
            correct += 1;
            document.getElementById("answer").innerHTML = "correct";

        } else {
            document.getElementById("answer").innerHTML = "try again";
        }
    }
// document.getElementById("total").innerHTML = `You got ${correct} correct!`;

};