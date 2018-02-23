let players = [];
let player_list = document.getElementById("player_list");
let add_player_bt = document.querySelector('#add_player_bt');
let new_player = document.querySelector('new_player');

add_player_bt.onclick = function() {
    let name = new_player.value;
    let li = document.createElement("li");
    li.innerText = name;
    player_list.appendChild(li);
    players.push({name: name, chips: 3}); // first is the property, the second is the value.
    console.log(players);
};

function roll_die () {
    let die = [".", ".", ".", "L", "C", "R"];
    let random_index = Math.floor(Math.random() * die.length);
    let random_die = die[random_index];
    return random_die;
}

function play_game() {
 //start with a random player

 //Loop through the players

 //calculate the number of dice based on their chips


//Roll dice and move chips
    // Check if winner

}

function number_of_dice(player) {   // return (player.chips >= 3)? 3: player.chips;
    let chips = player.chips;
    if(chips >= 3 ) {
        return 3;
    }
    return chips;
}

function left_player(player_index) {
    let left_index = player_index -1;
    if (left_index < 0) {
        left_index = left_index + players.length;
    }
    return left_index;
}

function right_player(player_inder) {
    let right_index = player_index + 1;
    if (right_index >= players.length) {
        right_index = right_index - players.length;
    }
    return right_index;
}