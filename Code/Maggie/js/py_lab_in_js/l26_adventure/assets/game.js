let board = document.querySelector(".gameboard");

function buildGameBoard() {
     for ( y = 0; y < 10; y++) {
        for (x = 0; x < 10; x++) {
            // console.log(`x:${x}, y:${y}`);
        gridcell = document.createElement('div');
        gridcell.className = 'col' + x + ' row' + y;
        // gridcell.innerText = `x:${x}, y:${y}`;
        gridcell.innerText = ".";
        // console.log(gridcell);
        board.appendChild(gridcell)
        }
    }
}
// function redCell() {
//     board.querySelector(".col5.row5").style.background = 'red';
//     console.log('redCell ran!')
// }
// board.addEventListener('click', redCell);

// function drawBackground() {
//     for (y)
// }

// window.onload(+





function changeBackground(color) {
   document.body.style.background = color; }
function changeColor(color) {
   document.body.style.color = color; }

changeBackground("black");
changeColor("white");
buildGameBoard();

const names = ['mike', 'vere', 'marcy', 'kim', 'joy', 'mildred', 'marty', 'Jeff', 'Manny', 'megan', 'mad max', 'Moore',
     'junior', 'Minty', 'myspace tom', 'Hugh Jass', 'john', 'jacob', 'jingleheimer', 'smith', 'Morticia',
     'Rick', 'Morty', 'jon smith', 'not sure', 'Beef Supreme', 'Mob', 'Toffle', 'moore'];

class PlayerCharacter {
    constructor(player_x, player_y) {
    this.player_x = player_x;
    this.player_y = player_y;
    this.drawCharacter(this.player_x, this.player_y);
    this.energy = 10;  //start with 10 energy
    }

    clearCharacter() {
        board.querySelector(`.col${this.player_x}.row${this.player_y}`).innerText = '.';
        console.log(`. drawn at ${this.player_x}, ${this.player_y} `);
    }

    drawCharacter() {
        board.querySelector(`.col${this.player_x}.row${this.player_y}`).innerText = '@';
        console.log(`@ drawn at ${this.player_x}, ${this.player_y} `);
    }

    get location() {
        console.log(`get location ${this.player_x}, ${this.player_y}`);
        return [this.player_x, this.player_y];
    }

    check_move(dx, dy) {
        let move_x = this.player_x + dx;
        let move_y = this.player_y + dy;
        return [move_x, move_y];
    }
    move(dx, dy) {
        let move = this.check_move(dx, dy);
        console.log(`at location x:${move[0]}, y:${move[1]} ${getStrAtLoc(move[0], move[1])}`);
        if (getStrAtLoc(move[0], move[1]) === '.') {
        // if (!(this.player_x + dx) instanceof NPC.location) {
            this.clearCharacter();
            this.player_x += dx;
            this.player_y += dy;
            this.drawCharacter();
        }
        else if (getStrAtLoc(move[0], move[1]) === '☺') {
            console.log("player chats with NPC")
        }

    }

}
function getStrAtLoc(x, y) {
    return board.querySelector(`.col${x}.row${y}`).innerText;
}

class NPC {
    constructor(name, x_location, y_location) {
        this.name = name;
        this.x_location = x_location;
        this.y_location = y_location;
        this.drawCharacter(this.x_location, this.y_location);
    }

    clearCharacter() {
        board.querySelector(`.col${this.x_location}.row${this.y_location}`).innerText = '.';
        console.log(`. drawn at ${this.x_location}, ${this.y_location} `);
    }

    drawCharacter() {
        board.querySelector(`.col${this.x_location}.row${this.y_location}`).innerText = '☺';
        console.log(`@ drawn at ${this.x_location}, ${this.y_location} `);
    }

    // get name() {
    // return this.name;
    // }

    get location() {
        console.log(`get location ${this.x_location}, ${this.y_location}`);
        return [this.x_location, this.y_location];
    }



    move(dx, dy) {
            this.clearCharacter();
            console.log("");
            this.player_x += dx;
            this.player_y += dy;
            this.drawCharacter();
        }
    // }

    // chat() {
    //     console.log(this.name + 'chats')
    // }

}

let player = new PlayerCharacter(5,5);
let Charlie = new NPC('Charlie', 2, 1);

window.onkeyup = function(e) {
   let key = e.keyCode ? e.keyCode : e.which;

  if (key === 37) {
       player.move(-1,0);
  }
   else if (key === 38) {
       player.move(0,-1);
  }
  else if (key === 39) {
       player.move(1,0);
  }
   else if (key === 40) {
       player.move(0, 1);
  }
};


// player.move(1,1);

// player_x = board.querySelector(".col5.row5").innerText = '@';

// (`.col${x}.row${y}`);

