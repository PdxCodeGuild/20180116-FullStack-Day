//
// Blackjack Simulator
//

let card_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
let card_obj = {'A': 0, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
let playerHand = {playerCards: [], playerTotal: 0};
let compHand = {compCards: [], compTotal: 0};
let bt_hit = document.querySelector("#bt_hit");     // buttons pushed by user
let bt_stay = document.querySelector("#bt_stay");
let card_div = document.querySelector('#cards_go_here');

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

        for (i=0; i<playerHand.playerCards.length; i++) {
            playerHand.playerTotal += card_obj[playerHand.playerCards[i]];
        }

        if (playerHand.playerTotal < 12) {
            let ace_value = 11;
            playerHand.playerTotal += 11;
            playerHand.playerCards.push('A');
            console.log("Ace value: " + ace_value);
            card_div.innerHTML += "<p>Ace value: " + ace_value + "</p>";
        } else {
            let ace_value = 1;
            playerHand.playerTotal += 1;
            playerHand.playerCards.push('A');
            console.log("Ace value: " + ace_value);
            card_div.innerHTML += "<p>Ace value: " + ace_value + "</p>";
        }
    }
    else {
        for (i=0; i < playerHand.playerCards.length; i++) {
            playerHand.playerTotal += card_obj[playerHand.playerCards[i]];
        }
    }

    console.log("The cards drawn are: " + playerHand.playerCards);
    console.log("The current total is: " + playerHand.playerTotal);
    card_div.innerHTML += "<p>The cards drawn are: " + playerHand.playerCards + "</p>";
    card_div.innerHTML += "<p>The current total is: " + playerHand.playerTotal + "</p>";
    return playerHand;
}

function compPlay(compHand) {
    if(compHand.compCards.includes('A')) {
        let value = 'A';
        compHand.compCards = compHand.compCards.filter(item => item !== value);

        for (i=0; i<compHand.compCards.length; i++) {
            compHand.compTotal += card_obj[compHand.compCards[i]];
        }

        if (compHand.compTotal < 12) {
            let ace_value = 11;
            compHand.compTotal += 11;
            compHand.compCards.push('A');
            console.log("Ace value: " + ace_value);
            card_div.innerHTML += "<p>Ace value: " + ace_value + "</p>";
        } else {
            let ace_value = 1;
            compHand.compTotal += 1;
            compHand.compCards.push('A');
            console.log("Ace value: " + ace_value);
            card_div.innerHTML += "<p>Ace value: " + ace_value + "</p>";
        }
    }
    else {
        for (i=0; i < compHand.compCards.length; i++) {
            compHand.compTotal += card_obj[compHand.compCards[i]];
        }
    }

    console.log("The cards drawn are: " + compHand.compCards);
    console.log("The computer's current total is: " + compHand.compTotal);
    card_div.innerHTML += "<p>The cards drawn are: " + playerHand.playerCards + "</p>";
    card_div.innerHTML += "<p>The computer's current total is: " + playerHand.playerTotal + "</p>";
    return compHand;
}


function startGame() {
    playerHand = {playerCards: [], playerTotal: 0};
    console.log("Starting game. Press 'hit' to get a card.");
    card_div.innerHTML += "<p>Starting game. Press 'hit' to get a card.</p>";
    return playerHand;
}

function hit(playerHand) {
    let new_card = deal();
    console.log("The card dealer gives you: " + new_card);
    card_div.innerHTML += "<p>The card dealer gives you: " + new_card + "</p>";
    playerHand.playerCards.push(new_card);
    play(playerHand);
    checkTotal(playerHand.playerTotal);
    return playerHand;
}

function stay(playerHand) {
    console.log("Stay. Your total is: " + playerHand.playerTotal);
    card_div.innerHTML += "<p>Stay. Your total is: " + playerHand.playerTotal + "</p>";
    checkTotal(playerHand.playerTotal);
    console.log("Now it's the computer's turn!");
    card_div.innerHTML += "<p>Now it's the computer's turn!</p>";
    compGame();
    return playerHand;
}

function checkTotal(total) {
    if (total === 21) {
        console.log("Blackjack!");
        console.log("Now it's the computer's turn!");
        card_div.innerHTML += "<p>Blackjack!</p>";
        card_div.innerHTML += "<p>Now it's the computer's turn!</p>";
        compGame();
    } else if (total > 21) {
        console.log("Busted :(");
        console.log("Now it's the computer's turn!");
        card_div.innerHTML += "<p>Busted :(</p>";
        card_div.innerHTML += "<p>Now it's the computer's turn!</p>";
        compGame();
    }
}


function compGame() {
    compHand = {compCards: [], compTotal: 0};

    while (hit === true) {
        let new_card = deal();
        console.log("<p>The computer gets: " + new_card + "</p>");
        compHand.compCards.push(new_card);
        compPlay(compHand);

        if (compHand.compTotal > 21) {
            console.log("Computer busted!");
            card_div.innerHTML += "<p>Computer busted!</p>";
            hit = false;
            break;
        } else if (compHand.compTotal === 21) {
            console.log("Computer gets Blackjack!");
            card_div.innerHTML += "<p>Computer gets Blackjack!</p>";
            hit = false;
            break;
        } else if (compHand.compTotal >= 17) {
            console.log("Computer stays");
            card_div.innerHTML += "<p>Computer stays</p>";
            hit = false;
            break;
        } else {
            console.log("Computer hits");
            card_div.innerHTML += "<p>Computer hits</p>";
            hit = true;
        }
    }
    return compHand;
}

// Original version - didn't work
// function game() {
//     let cards = [];
//     let hitting = true;
//     let total = 0;
//     let choice = '';
//     // this loop did not wait for player input
//     while (hitting === true) {
//         let new_card = deal();
//         console.log("The card dealer gives you: " + new_card);
//         cards.push(new_card);
//         total = play(cards);
//         // wait for user input
//         console.log("Do you hit or stay?");
//
//         let hit = document.querySelector("#bt_hit");
//         let stay = document.querySelector("#bt_stay");
//         hit.onclick = function(){
//             choice = "stay";
//         };
//         stay.onclick = function(){
//             choice = "hit";
//         };
//
//         if (total > 21) {
//             console.log("Busted! 😞");
//             hitting = false;
//             break;
//         } else if (total === 21) {
//             console.log("Blackjack!");
//             hitting = false;
//             break;
//         } else if (choice === 'stay') {
//             console.log("Stay");
//             hitting = false;
//             break;
//         } else if (choice === 'hit') {
//             console.log("Hit");
//             hitting = true;
//         } else {
//             console.log("Not a valid choice");
//         }
//     }
//     return total;
// }



// Load when ready.
$( document ).ready(function() {
    console.log( "ready!" );
    $("#bt_deal").click(function() {
        console.log("Dealing");
        card_div.innerHTML = "<p>Dealing</p>";
        startGame();
    });
    document.getElementById('bt_hit').addEventListener('click', function() {
        bt_hit.onclick = hit(playerHand);
    });
    document.getElementById('bt_stay').addEventListener('click', function() {
        bt_stay.onclick = stay(playerHand);
    });
});


// this makes the fancy pop-up footer work
jQuery(function($) {
	var open = false;
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
