//
// Blackjack Simulator
//

let card_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];
let card_obj = {'A': 0, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10};
let card_img = {'A': 'A.png', '2': '2.png', '3': '3.png', '4': '4.png', '5': '5.png', '6': '6.png', '7': '7.png', '8': '8.png', '9': '9.png', '10': '10.png', 'J': 'J.png', 'Q': 'Q.png', 'K': 'K.png'};
let aceCount = 0;
let compAceCount = 0;
let playerHand = {playerCards: [], playerTotal: 0};
let compHand = {compCards: [], compTotal: 0};
let bt_hit = document.querySelector("#bt_hit");     // buttons pushed by user
let bt_stay = document.querySelector("#bt_stay");
// let card_cont = document.querySelector('#card_cont');
let human_card_div = document.querySelector('#human_cards_go_here');    // div where the cards go
let comp_card_div = document.querySelector('#comp_cards_go_here');    // div where the cards go
let humanScore = document.querySelector("#humanScore");
let compScore = document.querySelector("#compScore");
let humanResult = document.querySelector("#human_result");
let compResult = document.querySelector("#comp_result");
let result = document.querySelector("#result");

// add dramatic pauses
function pause(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

//     Less than 17, advise to "Hit"
//     Over or equal to 17, advise to "Stay"
//     Exactly 21, advise "Blackjack!"
//     Over 21, advise "Already Busted"


// blackjack gameplay
function deal() {
    return card_list[Math.floor(Math.random() * card_list.length)];
}

// the human game (event-dependent)
function play(playerHand) {
    if (aceCount === 3) {
        let value = 'A';
        playerHand.playerCards = playerHand.playerCards.filter(item => item !== value);
        playerHand.playerTotal = 0;
        for (i=0; i<playerHand.playerCards.length; i++) {
            playerHand.playerTotal += card_obj[playerHand.playerCards[i]];
        }

        if (playerHand.playerTotal < 11) {
            let ace_value = 13;
            playerHand.playerTotal += 13;
            playerHand.playerCards.push('A');
            playerHand.playerCards.push('A');
            playerHand.playerCards.push('A');
            console.log("Aces value: " + ace_value);
        } else {
            let ace_value = 3;
            playerHand.playerTotal += 3;
            playerHand.playerCards.push('A');
            playerHand.playerCards.push('A');
            playerHand.playerCards.push('A');
            console.log("Aces value: " + ace_value);
        }
    } else if (aceCount === 2) {
        let value = 'A';
        playerHand.playerCards = playerHand.playerCards.filter(item => item !== value);
        playerHand.playerTotal = 0;
        for (i=0; i<playerHand.playerCards.length; i++) {
            playerHand.playerTotal += card_obj[playerHand.playerCards[i]];
        }

        if (playerHand.playerTotal < 11) {
            let ace_value = 12;
            playerHand.playerTotal += 12;
            playerHand.playerCards.push('A');
            playerHand.playerCards.push('A');
            console.log("Aces value: " + ace_value);
        } else {
            let ace_value = 2;
            playerHand.playerTotal += 2;
            playerHand.playerCards.push('A');
            playerHand.playerCards.push('A');
            console.log("Aces value: " + ace_value);
        }
    } else if (aceCount === 1) {
        let value = 'A';
        playerHand.playerCards = playerHand.playerCards.filter(item => item !== value);
        playerHand.playerTotal = 0;
        for (i=0; i<playerHand.playerCards.length; i++) {
            playerHand.playerTotal += card_obj[playerHand.playerCards[i]];
        }

        if (playerHand.playerTotal < 11) {
            let ace_value = 11;
            playerHand.playerTotal += 11;
            playerHand.playerCards.push('A');
            console.log("Ace value: " + ace_value);
        } else {
            let ace_value = 1;
            playerHand.playerTotal += 1;
            playerHand.playerCards.push('A');
            console.log("Ace value: " + ace_value);
        }
    }
    else {
        playerHand.playerTotal = 0;
        for (i=0; i < playerHand.playerCards.length; i++) {
            playerHand.playerTotal += card_obj[playerHand.playerCards[i]];
        }
    }

    console.log("The cards drawn are: " + playerHand.playerCards);
    console.log("The current total is: " + playerHand.playerTotal);
    humanScore.innerText = playerHand.playerTotal;
    return playerHand;
}

async function compPlay(compHand) {
    if (compAceCount === 3) {
        let value = 'A';
        compHand.compCards = compHand.compCards.filter(item => item !== value);
        compHand.compTotal = 0;
        for (i=0; i<compHand.compCards.length; i++) {
            compHand.compTotal += card_obj[compHand.compCards[i]];
        }

        if (compHand.compTotal < 11) {
            let ace_value = 13;
            compHand.compTotal += 13;
            compHand.compCards.push('A');
            compHand.compCards.push('A');
            compHand.compCards.push('A');
            console.log("Aces value: " + ace_value);
        } else {
            let ace_value = 3;
            compHand.compTotal += 3;
            compHand.compCards.push('A');
            compHand.compCards.push('A');
            compHand.compCards.push('A');
            console.log("Aces value: " + ace_value);
        }
    } else if (compAceCount === 2) {
        let value = 'A';
        compHand.compCards = compHand.compCards.filter(item => item !== value);
        compHand.compTotal = 0;
        for (i=0; i<compHand.compCards.length; i++) {
            compHand.compTotal += card_obj[compHand.compCards[i]];
        }

        if (compHand.compTotal < 11) {
            let ace_value = 12;
            compHand.compTotal += 12;
            compHand.compCards.push('A');
            compHand.compCards.push('A');
            console.log("Aces value: " + ace_value);
        } else {
            let ace_value = 2;
            compHand.compTotal += 2;
            compHand.compCards.push('A');
            compHand.compCards.push('A');
            console.log("Aces value: " + ace_value);
        }
    } else if (compAceCount === 1) {
        let value = 'A';
        compHand.compCards = compHand.compCards.filter(item => item !== value);
        compHand.compTotal = 0;
        for (i=0; i<compHand.compCards.length; i++) {
            compHand.compTotal += card_obj[compHand.compCards[i]];
        }

        if (compHand.compTotal < 11) {
            let ace_value = 11;
            compHand.compTotal += 11;
            compHand.compCards.push('A');
            console.log("Ace value: " + ace_value);
        } else {
            let ace_value = 1;
            compHand.compTotal += 1;
            compHand.compCards.push('A');
            console.log("Ace value: " + ace_value);
        }
    }
    else {
        compHand.compTotal = 0;
        for (i=0; i < compHand.compCards.length; i++) {
            compHand.compTotal += card_obj[compHand.compCards[i]];
        }
    }

    console.log("The cards drawn are: " + compHand.compCards);
    console.log("The computer's current total is: " + compHand.compTotal);
    compScore.innerText = compHand.compTotal;
    await pause(2200);
    return compHand;
}


function startGame() {
    playerHand = {playerCards: [], playerTotal: 0};
    console.log("Starting game. Press 'hit' to get a card.");
    result.innerText = "Starting game. Press 'Hit' to get a card, 'Stay' to finish your turn.";
    return playerHand;
}

function hit(playerHand) {
    result.innerText = "";
    let new_card = deal();
    console.log("The card dealer gives you: " + new_card);
    if (new_card === 'A') {
        aceCount += 1;
        console.log("Ace count: " + aceCount);
    }
    // make card show up on the board
    let newCardImg = document.createElement('img');
    let currentCard = card_img[new_card];
    newCardImg.setAttribute('src', 'img/playingCards/' + currentCard);
    newCardImg.setAttribute('class', 'animated slideInLeft');
    human_card_div.appendChild(newCardImg);
    playerHand.playerCards.push(new_card);
    // play the new card
    play(playerHand);
    checkTotal(playerHand.playerTotal);
    return playerHand;
}

async function stay(playerHand) {
    console.log("Stay. Your total is: " + playerHand.playerTotal);
    humanResult.innerText = "Stay. Your total is: " + playerHand.playerTotal;
    await pause(2200);
    checkTotal(playerHand.playerTotal);
    console.log("Now it's the computer's turn!");
    result.innerText = "Now it's the computer's turn!";
    await pause(2200);
    compGame();
    return playerHand;
}

async function checkTotal(total) {
    if (total === 21) {
        console.log("Blackjack!");
        console.log("Now it's the computer's turn!");
        humanResult.innerText = "Blackjack!";
        result.innerText = "Now it's the computer's turn!";
        humanResult.innerHTML = "<h4 class='animated tada'>Blackjack!</h4>";
        await pause(3000);
        compGame();
    } else if (total > 21) {
        console.log("Busted :(");
        console.log("Now it's the computer's turn!");
        humanResult.innerText = "Busted :(";
        result.innerText = "Now it's the computer's turn!";
        await pause(1200);
        humanResult.innerHTML = "<h4 class='animated hinge'>Busted :(</h4>";
        await pause(3000);
        humanResult.innerText = "Busted :(";
        compGame();
    }
}

// the computer game (automated)
async function compGame() {
    result.innerText = "";
    compHand = {compCards: [], compTotal: 0};
    let hit = true;

    while (hit === true) {
        let new_card = deal();
        console.log("The computer gets: " + new_card);
        if (new_card === 'A') {
            compAceCount += 1;
            console.log("Comp ace count: " + compAceCount);
        }
        // make card show up on the board
        let newCardImg = document.createElement('img');
        let currentCard = card_img[new_card];
        newCardImg.setAttribute('src', 'img/playingCards/' + currentCard);
        newCardImg.setAttribute('class', 'animated slideInRight');
        comp_card_div.appendChild(newCardImg);
        compHand.compCards.push(new_card);
        compPlay(compHand);

        if (compHand.compTotal > 21) {
            console.log("Computer busted!");
            compResult.innerText = "Computer busted!";
            await pause(2200);
            checkWinner(compHand);
            hit = false;
            break;
        } else if (compHand.compTotal === 21) {
            console.log("Computer gets Blackjack!");
            compResult.innerHTML = "<span class='animated tada'>Computer gets Blackjack!</span>";
            await pause(2200);
            checkWinner(compHand);
            hit = false;
            break;
        } else if (compHand.compTotal >= 17) {
            console.log("Computer stays");
            compResult.innerText = "Computer stays";
            await pause(2200);
            checkWinner(compHand);
            hit = false;
            break;
        } else {
            console.log("Computer hits");
            compResult.innerText = "Computer hits";
            await pause(2000);
            hit = true;
        }
    }
    return compHand;
}


async function checkWinner(compHand) {
    console.log("Checking winner");
    let winner = "";
    if (playerHand.playerTotal > compHand.compTotal && playerHand.playerTotal <= 21) {
        winner = "The human wins!";
        console.log(winner);
        result.innerText = winner;
        $('#human').addClass('animated bounce');
        await pause(3200);
        result.innerText = "Hit 'Deal' to play again!";
    } else if (compHand.compTotal > playerHand.playerTotal && compHand.compTotal <= 21) {
        winner = "The computer wins!";
        console.log(winner);
        result.innerText = winner;
        $('#comp').addClass('animated bounce');
        await pause(3200);
        result.innerText = "Hit 'Deal' to play again!";
    } else if (compHand.compTotal === playerHand.playerTotal) {
        winner = "It's a tie!";
        console.log(winner);
        result.innerText = winner;
        await pause(3200);
        result.innerText = "Hit 'Deal' to play again!";
    } else if (compHand.compTotal > 21 && playerHand.playerTotal > 21) {
        winner = "Both players busted";
        console.log(winner);
        result.innerText = winner;
        await pause(3200);
        result.innerText = "Hit 'Deal' to play again!";
    } else if (compHand.compTotal > 21) {
        winner = "The human wins!";
        console.log(winner);
        result.innerText = winner;
        $('#human').addClass('animated bounce');
        await pause(3200);
        result.innerText = "Hit 'Deal' to play again!";
    }   else if (playerHand.playerTotal > 21) {
        winner = "The computer wins!";
        console.log(winner);
        result.innerText = winner;
        $('#comp').addClass('animated bounce');
        await pause(3200);
        result.innerText = "Hit 'Deal' to play again!";
    } else {
        winner = "Hit 'Deal' to play again!"
        console.log(winner);
        result.innerText = winner;
    }
    return winner;
}


// Load when ready.
$( document ).ready(function() {
    console.log( "ready!" );
    $("#bt_deal").click(function() {
        // reset everything when new hand dealt
        aceCount = 0;
        compAceCount = 0;
        $('#human').removeClass('animated bounce');
        $('#comp').removeClass('animated bounce');
        humanScore.innerText = 0;
        compScore.innerText = 0;
        human_card_div.innerHTML = '';
        comp_card_div.innerHTML = '';
        humanResult.innerText = "";
        compResult.innerText = "";
        console.log("Dealing");
        startGame();
    });
    bt_hit.addEventListener('click', function() {bt_hit.onclick = hit(playerHand);});
    bt_stay.addEventListener('click', function() {bt_stay.onclick = stay(playerHand);});
});


// this makes the fancy pop-up footer work
jQuery(function($) {
	let open = false;
	$('#footerSlideButton').click(function () {
		if(open === false) {
			if(Modernizr.csstransitions) {
				$('#footerSlideContent').addClass('open');
			} else {
				$('#footerSlideContent').animate({ height: '25vh' });
			}
			$(this).css('backgroundPosition', 'bottom left');
			open = true;
		} else {
			if(Modernizr.csstransitions) {
				$('#footerSlideContent').removeClass('open');
			} else {
				$('#footerSlideContent').animate({ height: '0px' });
			}
			$(this).css('backgroundPosition', 'top left');
			open = false;
		}
	});
});


// activate dark mode!
$('#bt_dark').click(function() {
    $('body').addClass('darkTheme');
    $('#wrapper').removeClass('wrapper');
    $('#wrapper').addClass('darkTheme');
    $('#card_cont').removeClass('card_cont');
    $('#card_cont').addClass('darkTheme');
});
