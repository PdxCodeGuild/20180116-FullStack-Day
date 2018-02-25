// python lab 007 rock paper scissors javascript conversion

let hands = ["rock", "paper", "scissors"];

let userHand;
userHand = [];

let x = true;

while (x) {
    userHand = [];
    alert("lets play rock paper scissors");
    //user chooses weapon, which gets added to userHand
    switch (prompt("choose ur weapon: rock, paper, or scissors")) {
        case "rock":
            userHand.push("rock");
            break;
        case "paper":
            userHand.push("paper");
            break;
        case "scissors":
            userHand.push("scissors");
            break;
    }
    //opponents weapon is random
    let opponent = hands[Math.floor(Math.random() * hands.length)];
    alert("ur opponents weapon is " + opponent + "! o shyt!");

    // opponent rock
    if (opponent === "rock") {
        switch (userHand[0]) {
            case "paper":
                alert("ur paper > opponents rock. victory!");
                break;
            case "scissors":
                alert("opponents rock > ur scissors. defeat!");
                break;
            case "rock":
                alert("ur rock = opponents rock. draw!");
                break;
        }
    }

    // opponent paper
    if (opponent === "paper") {
        switch (userHand[0]) {
            case "paper":
                alert("ur paper = opponents paper. draw!");
                break;
            case "scissors":
                alert("ur scissors > opponents paper. victory!");
                break;
            case "rock":
                alert("opponents paper > ur rock. defeat!");
                break;
        }
    }

    //opponent scissors
    else if (opponent === "scissors") {
        switch (userHand[0]) {
            case "paper":
                alert("opponents scissors > ur paper. defeat!");
                break;
            case "scissors":
                alert("ur scissors = opponents scissors. draw!");
                break;
            case "rock":
                alert("ur rock > opponents scissors. victory!");
                break;
        }
    }

    // play again
    // let again =["yes", "no"];
    // again = [];

    if(confirm("u wanna play again?")) {
        alert("woo lets doit!");
    }
    else {
        alert("thx 4 playing! bai!");
        x = false;
    }
}
