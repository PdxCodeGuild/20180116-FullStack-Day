let players = [];
let center_chips = 0;
let player_list = document.getElementById("player_list");
let add_player_bt = document.querySelector('#add_player_bt');
let new_player = document.querySelector('new_player');
let play_game_bt = document.querySelector('#play_game_bt');


add_player_bt.onclick = function() {
    let name = new_player.value;
    let li = document.createElement("li");
    li.innerText = name;
    player_list.appendChild(li);
    players.push({name: name, chips: 3}); // first is the property, the second is the value.
    console.log(players);
};

play_game_bt.onclick = function () {
    play_game();
};

function printLine(line) {
    output_text.innerText += line + 'n\';
}

function roll_die () {
    let die = [".", ".", ".", "L", "C", "R"];
    let random_index = Math.floor(Math.random() * die.length);
    return die[random_index];
}

function play_game() {
 //start with a random player
  let player_index = Math.floor(Math.random() * players.length);
 //Loop through the players
 while (!check_win()) {
     let player = players[player_index];
     let leftPlayer = players[left_player(player_index)];
     let rightPlayer = players[right_player(player_index)];
     let n_dice = number_of_dice(players[player_index]);
     for (let i=0; i < n_dice; ++i) {
         let die = roll_die();
         if (die = 'L'){
             player.chips -= 1;
             leftPlayer.chips += 1;
         }
         else if (die = 'R') {
             player.chips -= 1;
             rightPlayer.chips += 1;
         }
         else if (die = 'C') {
             player.chips -= 1;
             center_chips += 1;
         }
      }
     player_index = rightPlayer(player_index);

     let winningPlayer = checkWin();
     alert(winningPlayer.name + "has won!!! Hurrrraaaaay!")
 }
 //calculate the number of dice based on their chips;
    // loop - roll the dice
    // mainLoop chips
    // check for winner

}

function check_win () {
    let winner = [];
    for (let i=0; 1 < players.length; ++i) {
        if (players[i].chips >0) {
            winner.push(players[i]);
        }
    }
    return (winner.length === 1)? winner[0]: null;
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

function right_player(player_index) {
    let right_index = player_index + 1;
    if (right_index >= players.length) {
        right_index = right_index - players.length;
    }
    return right_index;
}

