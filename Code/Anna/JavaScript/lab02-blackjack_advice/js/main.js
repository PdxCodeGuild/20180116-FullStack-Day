//
// Blackjack Simulator
// Ascii art: https://www.ascii-code.com/ascii-art/miscellaneous/playing-cards.php
//

let card_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];
let card_obj = {'A': 0, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10};
let card_img = {'A': 'A.png', '2': '2.png', '3': '3.png', '4': '4.png', '5': '5.png', '6': '6.png', '7': '7.png', '8': '8.png', '9': '9.png', '10': '10.png', 'J': 'J.png', 'Q': 'Q.png', 'K': 'K.png'};
let playerHand = {playerCards: [], playerTotal: 0};
let compHand = {compCards: [], compTotal: 0};
let bt_hit = document.querySelector("#bt_hit");     // buttons pushed by user
let bt_stay = document.querySelector("#bt_stay");
let card_cont = document.querySelector('#card_cont');
let human_card_div = document.querySelector('#human_cards_go_here');    // div where the cards go
let comp_card_div = document.querySelector('#comp_cards_go_here');    // div where the cards go
let humanScore = document.querySelector("#humanScore");
let compScore = document.querySelector("#compScore");
let humanResult = document.querySelector("#human_result");
let compResult = document.querySelector("#comp_result");
let result = document.querySelector("#result");


function pause() {
    return new Promise(resolve => setTimeout(resolve, 2000));
}

//     Less than 17, advise to "Hit"
//     Over or equal to 17, advise to "Stay"
//     Exactly 21, advise "Blackjack!"
//     Over 21, advise "Already Busted"


function deal() {
    return card_list[Math.floor(Math.random() * card_list.length)];
}

function play(playerHand) {
    if(playerHand.playerCards.includes('A')) {
        let value = 'A';
        playerHand.playerCards = playerHand.playerCards.filter(item => item !== value);
        playerHand.playerTotal = 0;
        for (i=0; i<playerHand.playerCards.length; i++) {
            playerHand.playerTotal += card_obj[playerHand.playerCards[i]];
        }

        if (playerHand.playerTotal < 12) {
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
    if(compHand.compCards.includes('A')) {
        let value = 'A';
        compHand.compCards = compHand.compCards.filter(item => item !== value);
        compHand.compTotal = 0;
        for (i=0; i<compHand.compCards.length; i++) {
            compHand.compTotal += card_obj[compHand.compCards[i]];
        }

        if (compHand.compTotal < 12) {
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
    await pause();
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
    // make card show up on the board
    let newCardImg = document.createElement('img');
    let currentCard = card_img[new_card];
    newCardImg.setAttribute('src', 'img/playingCards/' + currentCard);
    human_card_div.appendChild(newCardImg);
    playerHand.playerCards.push(new_card);
    play(playerHand);
    checkTotal(playerHand.playerTotal);
    return playerHand;
}

async function stay(playerHand) {
    console.log("Stay. Your total is: " + playerHand.playerTotal);
    humanResult.innerText = "Stay. Your total is: " + playerHand.playerTotal;
    await pause();
    checkTotal(playerHand.playerTotal);
    console.log("Now it's the computer's turn!");
    result.innerText = "Now it's the computer's turn!";
    await pause();
    compGame();
    return playerHand;
}

async function checkTotal(total) {
    if (total === 21) {
        console.log("Blackjack!");
        console.log("Now it's the computer's turn!");
        humanResult.innerText = "Blackjack!";
        await pause();
        result.innerText = "Now it's the computer's turn!";
        compGame();
    } else if (total > 21) {
        console.log("Busted :(");
        console.log("Now it's the computer's turn!");
        humanResult.innerText = "Busted :(";
        await pause();
        result.innerText = "Now it's the computer's turn!";
        compGame();
    }
}


async function compGame() {
    result.innerText = "";
    compHand = {compCards: [], compTotal: 0};
    let hit = true;

    while (hit === true) {
        let new_card = deal();
        console.log("The computer gets: " + new_card);
        // make card show up on the board
        let newCardImg = document.createElement('img');
        let currentCard = card_img[new_card];
        newCardImg.setAttribute('src', 'img/playingCards/' + currentCard);
        comp_card_div.appendChild(newCardImg);
        compHand.compCards.push(new_card);
        await pause();
        compPlay(compHand);

        if (compHand.compTotal > 21) {
            console.log("Computer busted!");
            compResult.innerText = "Computer busted!";
            checkWinner(playerHand, compHand);
            hit = false;
            break;
        } else if (compHand.compTotal === 21) {
            console.log("Computer gets Blackjack!");
            compResult.innerText = "Computer gets Blackjack!";
            checkWinner(playerHand, compHand);
            hit = false;
            break;
        } else if (compHand.compTotal >= 17) {
            console.log("Computer stays");
            compResult.innerText = "Computer stays";
            checkWinner(playerHand, compHand);
            hit = false;
            break;
        } else {
            console.log("Computer hits");
            compResult.innerText = "Computer hits";
            hit = true;
        }
    }
    return compHand;
}


function checkWinner(playerHand, compHand) {
    console.log("Checking winner");
    let winner = "";
    if (21 >= playerHand.playerTotal > compHand.compTotal) {
        winner = "The human wins!";
        console.log(winner);
        result.innerText = winner;
    } else if (21 >= compHand.compTotal > playerHand.playerTotal) {
        winner = "The computer wins!";
        console.log(winner);
        result.innerText = winner;
    } else if (compHand.compTotal > 21 && playerHand.playerTotal > 21) {
        winner = "Both players busted";
        console.log(winner);
        result.innerText = winner;
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
				$('#footerSlideContent').animate({ height: '40vh' });
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
});
