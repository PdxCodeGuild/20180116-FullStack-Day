console.log('script');
//ROCK PAPER SCISSORS (RPS) JS V2

// game description:
	//user and computer attempt to defeat eachother in a battle of wits, wherein:
		//user makes a choice between r p s
		//computer player random choice between r p s
		//two choices are compared, winner is decided, x beats y
		//the user is() presented with the option to play again


//Selector Variables
let rock_div = document.querySelector("#rock_div");
let scissors_div = document.querySelector("#scissors_div");
let paper_div = document.querySelector("#paper_div");
let container_div = document.querySelector('#container_div');
let player_message_sp =  document.querySelector("#player_msg_sp");
let computer_message_sp = document.querySelector("#computer_msg_sp");
let play_again_div = document.querySelector('#play_again_div');
let computer_div = document.querySelector('#computer_div');
let player_div = document.querySelector('#player_div');
let action_message_div = document.querySelector('#action_message_div');
let outcome_message_div = document.querySelector('#outcome_message_div');
let msg1_sp = document.querySelector('#msg1_sp');
let msg2_sp = document.querySelector('#msg2_sp');
let msg1_icon = document.querySelector('#msg1_icon');
let msg2_icon = document.querySelector('#msg2_icon');

//global objects and variables
let choices = ['rock', 'paper', 'scissors'];
let winning = {'rock':'scissors', 'paper':'rock', 'scissors':'paper'}
let winning_actions = {'rock':'breaks', 'paper':'covers', 'scissors':'cuts'}

let rnd_choice_index = Math.floor(Math.random() * (choices.length + 1)); 
let outcomes = ['You lose :(','You win! :)', 'Draw :/']
let decided = false;

let user_choice = ''
let outcome = ''
let action = '';


//initial states
function initialize() {
	container_div.style.display = 'block';
	msg1_icon.style.display = 'inline-block';
	msg1_sp.innerText = 'choose your weapon!'
	play_again_div.style.display = "none";
	computer_div.style.display = "none";
	player_div.style.display = "none";
	msg2_icon.style.display = "none";

}
//set initial states
let start = initialize()

//div icon clicks
//capturing click inputs for choices, call to decide
rock_div.onclick = function () {
	user_choice = 'rock';
	pass(user_choice);
}
scissors_div.onclick = function () {
	user_choice = 'scissors';
	pass(user_choice);
}
paper_div.onclick = function () {
	user_choice = 'paper'
	pass(user_choice);
}

//play again click function, not shown until decided
play_again_div.onclick = function() {
	reset();
}

//helper function for displaying and passing choices
function pass(user_choice) {
	msg1_icon.style.display = 'none';
	container_div.style.display = 'none';
	//display user icon
	msg1_sp.innerText = ''
	//hide action text icon
	//display user choice	
	player_message_sp.innerText = `Player chooses ${user_choice}.`;
	player_div.style.display = "block";
	
	//wait and call decide
	setTimeout(function () { decide(user_choice)}, 
	500);
}

//decide(choice) updates action && outcome
function decide(user_choice) {
	//get random choice 
	let rnd_choice_index = Math.floor(Math.random() * (choices.length - 1));
	let random_choice = choices[rnd_choice_index];
	//display comp icon
	computer_div.style.display = "block";
	//display comp choice	
	computer_message_sp.innerText = `Computer chooses ${random_choice}.`;
	//compare user and comp choices
	if (user_choice === random_choice) { 
		outcome = outcomes[2];
	}
	else if (winning[user_choice] === random_choice) {
		outcome = outcomes[1];
		action =  `${user_choice} ${winning_actions[user_choice]} ${random_choice}.`
	}
	else {
		outcome = outcomes[0];
		action = `${random_choice} ${winning_actions[random_choice]} ${user_choice}.`;	
	}
	//decision has been made
	decided = true;
	//display action
	setTimeout( function() {
	msg1_sp.innerText = action}, 500);
	//wait and display outcome
	setTimeout( function() {
	msg2_icon.style.display = "inline-block";
	msg2_sp.innerText = outcome}, 500);
	//display play again button
	setTimeout( function() {
	play_again_div.style.display = "block"}, 1000);
	console.log(`decided:${decided}, user_choice:${user_choice}, outcome:${outcome} random_choice:${random_choice} action:${action}`);
}

//reset all the states
function reset() {
	initialize();
	decided = false;
	outcome = '';
	user_choice = '';
	msg2_sp.innerText = "";
}

// updates globals:[play_again_bt_message, player_msg,  ]
// play_again_div.onclick = function () {
// 	computer_message = 'Choose your weapon'
// }


// //definining variables for html fields
// let rps_input = document.querySelector('#rps_input');
// let play_bt = document.querySelector('#play_bt');
// let output_div = document.querySelector('#output_div');


// //comparison function... comparing indexes
// function compare(user_index, comp_choice_index) {
    
//   // let index = rps_list.indexOf(rps_input);
//     // invalid logic, also not extendable
//     // let result = (user_index - comp_choice_index) % 3;
//     // if (result == 1) {
//     //     output_div.innerText +='you win!!'
//     // }
//     // else if (result == 0) {
//     //    output_div.innerText +='you tied!'
//     // }
//     // else {
//     //    output_div.innerText +='Computer wins!!'
//     // }
//     // }

// let rps_list = ['rock', 'paper', 'scissors'];

  
  
// //when pressing 'play'
// play_bt.onclick = async function() {
//     //get user input
//     let rps_choice = rps_input.value;
//   //check if valid entry, valid if in rps_list
//     if (rps_list.includes(rps_choice)) {
//         output_div.innerText = 'You chose ' + rps_choice + '.\n';

//       //pause
//       await sleep(500);

//       let user_index = rps_list.indexOf(rps_choice);
//       let choose_index = Math.floor(Math.random()*3);
//       //random number between 1-3
//       //get comp
//       output_div.innerText += 'Computer chose ' + rps_list[choose_index] + '.\n';

//          //pause
//       await sleep(500);

//       //compare choices
//       compare(user_index, choose_index);
//     }

//     else {
//         output_div.innerText = 'Enter rock, paper, or scissors';
//     }
// }