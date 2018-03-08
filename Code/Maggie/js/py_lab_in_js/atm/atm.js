//ATM++ 

// User Cash: $500

let main_div = document.querySelector('#main_div');
let atm_div = document.querySelector('#atm_div');
let text_display_div = document.querySelector('#text_display_div');
let options_div

// ATM class
class ATM {
	constructor( balance, interest_rate ) {
		this.balance = balance;
		this.interest_rate = interest_rate;
	}
	get current_balance() {
		return this.balance;
	}
	get current_interest_rate() {
		return this.interest_rate;
	}
	deposit( amount ) {
		this.balance += amount;
		return this.balance;
	} 
	withdraw( amount ) {
		//withdraw requested amount if available
		return (this.balance - amount >= 0)? this.balance - amount: false; 
	}
	compute_interest() {
		this.balance += (this.balance * interest_rate);
		console.log (`rate ${interest_rate} applied`);
		return this.balance;
	}
};

let cityATM = new ATM(500, 1);

let welcome_msg = 'Thanks for using CityATM!';
let choice_head = 'choose from the following options';

// type_text(welcome_msg, text_display_div.innerText);

// function type_text(message, output_field) {
// 	for (i=0; i < message.length; i++) {
// 		setTimeout( function() {
// 		output_field += message[i] 
// 	}, 200);
// 	};
// }
