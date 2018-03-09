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

function createPageElement(parent_element, element_type, element_class, element_id) {
	//create any empty element on the page
	let element = document.createElement(element_type);
	element.className = element_class || null;
	element.id = element_id || null;
	document.querySelector(parent_element).appendChild(element);
	console.log(`created element: ${element_type} parent: ${parent_element} class: ${element_class} id: ${element_id}`);
}

function create_main_elements() {
	createPageElement('body', 'div', );
	document.querySelector('.container').onload(createPageElement('container', 'h1', 'main_text', 'main_text'));
	// const main_input_field = create_page_element('container', 'input', 'input_field', 'input_field');
	// const main_button = create_page_element('container', 'button', 'button', 'button');
}

function buildGameBoard2() {
    const gameBoardWidth = 10;
    const gameBoardHeight = 10;
    for ( y = 0; y < 10; y++)
     {
        for (let x = 0; x < 10; x++) {
            // console.log(`x:${x}, y:${y}`)
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

    move(dx, dy) {
        let move = this.check_move(dx, dy);
        console.log(`at location x:${move[0]}, y:${move[1]} ${getStrAtLoc(move[0], move[1])}`);
        if (getStrAtLoc(move[0], move[1]) === '.') {
            // if (!(this.player_x + dx) instanceof NPC.location) {
            this.clearCharacter();
            this.x_location += dx;
            this.y_location += dy;
            this.drawCharacter();
            // get name() {
            // return this.name;
        }
    }

    get location() {
        console.log(`get location ${this.x_location}, ${this.y_location}`);
        return [this.x_location, this.y_location];
    }


    // }

    // chat() {
    //     console.log(this.name + 'chats')
    // }

}

let player = new PlayerCharacter(5,5);
let Charlie = new NPC('Charlie', 2, 1);

window.onkeyup = function(event) {
   let key = event.keyCode ? event.keyCode : event.which;

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

