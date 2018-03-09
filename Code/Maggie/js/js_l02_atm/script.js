
// User Cash: $500

//selectors
let main_div = document.querySelector('#main_div');
let atm_div = document.querySelector('#atm_div');
let text_display_div = document.querySelector('#text_display_div');
let top_msg_sp =document.querySelector('#top_msg_sp');
let opt_sp = document.querySelector('#opt_sp');
let li_1 = document.querySelector('#li_1');
let li_2 = document.querySelector('#li_2');
let li_3 = document.querySelector('#li_3');
let li_4 = document.querySelector('#li_4');
let li_5 = document.querySelector('#li_5');
let return_li = document.querySelector('#return_li')
let output_sp = document.querySelector('#output_sp');

let withdraw_div = document.querySelector('#withdraw_div');
let withdraw_bt = document.querySelector('#withdraw_bt');
withdraw_div.style.display = 'none';

let deposit_div = document.querySelector('#deposit_div');
let deposit_bt = document.querySelector('#deposit_bt');
deposit_div.style.display = 'none';

let user_cash = 0;
// ATM class
class ATM {
	constructor( balance, interest_rate ) {
		this.balance = balance;
		this.interest_rate = interest_rate;
	}
	get current_balance() {
		return this.balance.toFixed(2);
	}
	get current_interest_rate() {
		return this.interest_rate;
	}
	deposit( amount ) {
		this.balance += parseInt(amount);
		return this.balance.toFixed(2);
	} 
	withdraw( amount ) {
		//withdraw requested amount if available
		amount = parseInt(amount);
		this.balance -= amount;
		// this.balance -= (this.balance - amount >= 0)? amount: 0; 
		return this.balance.toFixed(2)
	}
	compute_interest() {
		this.balance += (this.balance * this.interest_rate);
		console.log (`rate ${this.interest_rate} applied`);
		return this.balance.toFixed(2);
	}
}

//objects and variables
let cityATM = new ATM(500, 0.01);
let cash_on_hand = 0;

let welcome_msg = 'CityATM';
top_msg_sp.innerText = welcome_msg;

function list_options(){
	let ul_txt = 'choose from the following options:';
	let li_1_txt = '⇰ check balance'
	let li_2_txt = '⇰ check account interest rate'
	let li_3_txt = '⇰ deposit cash';
	let li_4_txt = '⇰ withdraw cash';
	let li_5_txt = '⇰ End Session.'
	let fields = [li_1, li_2, li_3, li_4, li_5]
	let messages = [li_1_txt, li_2_txt, li_3_txt, li_4_txt, li_5_txt];
	type_writer(ul_txt, opt_sp);
	setTimeout(function() { bullet_poster(messages, fields) }, 500);
};

function clear_options() {
	opt_sp.innerHTML = '';
	li_1.innerHTML = '';
	li_2.innerHTML = '';
	li_3.innerHTML = '';
	li_4.innerHTML = '';
	li_5.innerHTML = '';
	return_li.innerHTML = 'return to previous menu.'
	output_sp.innerHTML = '';
	return_li.innerHTML = '';
	withdraw_div.style.display = 'none';
	deposit_div.style.display = 'none';

};	

function type_writer(message, output_field) {
	let i = 0;
	setInterval( function() {
		if (i < message.length) {
			//get letter
		curr_letter = message[i];
		//put letter in field
		output_field.innerHTML += curr_letter;
		//update i
		i++}}, 20);
	clearInterval();
	};

function bullet_poster(messages, outputs) {
	let i = 0;
		setInterval( function() {
		if (i < messages.length) {
			//get letter
		curr_message = messages[i];
		//put letter in field
		outputs[i].innerHTML += curr_message;
		//update i
		i++}}, 500);
	clearInterval();
};


list_options();

let dispense_msg = 'Your cash has been dispensed in the tray beneath this machine.';
let uptake_msg = 'Ok, money has been deposited into your account.';

li_1.onclick = function () {
	clear_options();
	text= `Your current balance is $${cityATM.current_balance}`;
	type_writer(text,opt_sp);
	display_return();
};
li_2.onclick = function () {
	clear_options();
	cityATM.compute_interest();
	text= `The current interest rate for your account is ${cityATM.current_interest_rate * 100}% and has been applied to your balance.`
	type_writer(text,opt_sp);
	display_return();

};
li_3.onclick = function () {
	clear_options();
	text= `How much would you like to deposit?`;
	type_writer(text,opt_sp);
	deposit_div.style.display = 'block';
	display_return();
};
li_4.onclick = function () {
	clear_options();
	text= `How much would you like to withdraw?`;
	type_writer(text,opt_sp);
	withdraw_div.style.display = 'block';
	display_return();
};
li_5.onclick = function () {
	clear_options();
	text = 'Thanks for using CityATM!';
	type_writer(text,opt_sp);
};
return_li.onclick = function () {
	clear_options();
	list_options();
};
deposit_bt.onclick = function () {
	let deposit_value = document.querySelector('#deposit_input').value;
	deposit_value = parseInt(deposit_value);
	user_cash = cityATM.deposit(deposit_value);
	document.querySelector('#deposit_input').value = 0;
	clear_options()
	type_writer(uptake_msg, opt_sp);
	setTimeout(function () {
		clear_options();
		list_options();
	}, 1000)
};

withdraw_bt.onclick = function () {
	let withdraw_value = document.querySelector('#withdraw_input').value;
	withdraw_value = parseInt(withdraw_value);
	cityATM.withdraw(withdraw_value);
	document.querySelector('#withdraw_input').value = 0;
	clear_options()
	type_writer(dispense_msg, opt_sp);
	setTimeout(function () {
	clear_options();
	list_options();
	}, 1500)
};

function display_return() {
	text = '⇰ Return to previous menu';
	setTimeout(function () { return_li.innerHTML = text}, 1500);
}

//thanks for using city js_l02_atm
//choose from the following options:
//check current balance
//check the acount interest rate
//accrue interest
//deposit cash
//withdraw cash
