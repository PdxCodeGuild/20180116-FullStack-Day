
//Color palette
let board_black = 'rgb(39,40,34)'; //background
let board_white = 'rgb(214, 214, 214)'; //in view, empty

let color_swatch = {};
//color classes
color_swatch.pc = 'rgb(253,151,31)';
color_swatch.fauna = 'rgb(249,38,114)';

//init main colors
document.body.style.background = board_black;
document.body.style.color = board_white;

//html elements
let message_div = document.createElement('div');
let main = document.querySelector('.main')
main.appendChild(message_div);
message_div.setAttribute('class', 'message_div');
message_div.style.backgroundColor = board_black;
message_div.style.color = board_white;
message_div.style.fontSize = '20px';
message_div.innerText = 'Adventure Game! Use arrow keys to move.';


class Gameboard {
    constructor( width, height ) {
        this.width = width;
        this.height = height;
        this.gridcells = [];  //2d array of objects.

        for (let y = 0; y < height; y++) {
            this.gridcells[y] = [];
            for (let x = 0; x < height; x++) {
                this.gridcells[y][x] = new GridCell(x,y);
                // append an entry to a variable used to construct
            }
        }
    }
    gridcell(x,y) {
        // console.log(this.gridcells[y][x]);
        return this.gridcells[y][x]
    }
}

class GridCell {
    constructor(x, y){
        this.x = x;
        this.y = y;
        this.items = [];
        this.blocked = false;
    }

}

class Player {
    constructor(name, x, y) {
        this.name = name;
        this.x = x;
        this.y = y;
        this.char = '@';
        this.type = 'pc';
    }
    move(dx, dy) {
        let new_x = this.x + dx;
        let new_y = this.y + dy;
        let pivot = gameboard.gridcell(new_x, new_y);
        console.log(`pivot: character: ${pivot.character} blocked: ${pivot.blocked}`);
        console.log(pivot);
        if (pivot.blocked) {
            message_div.innerText = 'Want to play a game?';
        } else {
            this.x = new_x;
            this.y = new_y;
            render_entities()
        }
    }
}

class Entity {
    constructor(name, type, x, y) {
        this.name = name;
        this.type = type;
        this.character = false;
        this.touch_msg = 'you touched me';
        this.x = x;
        this.y = y;
        gameboard.gridcell(x, y).occupant = this;
    }
}

let gameboard = new Gameboard(10, 10);
let player = new Player('player', 5, 5);
let npc = new Entity('npc', 'fauna', 3, 3);
let entities = [player, npc];
npc.char = '*';
gameboard.gridcell(3,3).blocked = true;
render_gameboard();
render_character(player.x, player.y, player.char, color_swatch.pc);
render_character(npc.x, npc.y, npc.char, color_swatch[npc.type]);

//recieving functions
function render_gameboard( ) {
    let main_div = document.querySelector('.main');
    let gameboard_div = document.createElement('div'); //create node
    gameboard_div.setAttribute('class', 'gameboard');
    main_div.appendChild(gameboard_div); //add node to html
    for (let y = 0; y < gameboard.height; y++) {
        for (let x = 0; x < gameboard.width; x++) {  //iterate through 2d indices
            let cell_div = document.createElement('div'); //divs for cells
            cell_div.id = `x:${x} y:${y}`; //referencable for rendering
            cell_div.innerText = '.'; //just background
            gameboard_div.appendChild(cell_div);
        }
    }

}
function render_character(x, y, char, color, bg_color) {
    div_select = document.getElementById(`x:${x} y:${y}`);
    div_select.innerText = char;
    div_select.style.color = color;
    div_select.style.backgroundColor = bg_color || null;
}
function render_entities() {
    clear_gameboard();
    render_gameboard();
    for (let i = 0; i < entities.length; i++) {
        let ent = entities[i];
        render_character(ent.x, ent.y, ent.char, color_swatch[ent.type]);
    }
}

function clear_gameboard() {
    //select elements
    let board = document.querySelector('.gameboard');
    //remove them
    board.remove();
    message_div.innerText= '';
}
window.onkeydown = function(event) {
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