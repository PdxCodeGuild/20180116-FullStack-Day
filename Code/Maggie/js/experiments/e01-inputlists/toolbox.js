// console.log('script');

//colors!
//Color palette
let board_black = 'rgb(39,40,34)'; //background
let board_grey = 'rgb(80,80,80)';  //previously explored, remembered
let board_white = 'rgb(214, 214, 214)'; //in view, empty
let board_pink = 'rgb(249,38,114)'; //item
let board_blue = 'rgb(102,217,239)'; //water
let board_green = 'rgb(166,226,46)';   //flora
let board_orange = 'rgb(253,151,31)'; //npc entities
let board_yellow = 'rgb(244,222,117)'; //mineral scenery


//html helpers

//create single html elements
function createPageElement(parent_element, element_type, element_class, element_id) {
	//create the container and its children: header, input box, button
	let element = document.createElement(element_type);
	element.className = element_class || null;
	element.id = element_id || null;
	document.querySelector(parent_element).appendChild(element);
	console.log(`created element: ${element_type} parent: ${parent_element} class: ${element_class} id: ${element_id}`);
}

function deleteElement(element) {
    document.getElementById(element).remove();
    this.remove();
}

// -----------------------end html stuff

// <script src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/14082/FileSaver.js"></script>
function saveJSONArrayToCSV( objectsArray, filename ) {
	csv = objectsArray.map(function(data){
		return JSON.stringify(Object.values(data));
	}).join('\n')
	.replace(/(^\[)|(\]$)/mg, '');
	let blob = new Blob([csv], {type: "text/csv;charset=utf-8"});
    saveAs(blob, filename+".csv")
}

function saveArrayToCSV(dataarray, filename) {
    let csv = dataarray.map(function(data){
        return data.join();
    }).join('\n');
    let blob = new Blob([csv], {type: "text/csv;charset=utf-8"});
    saveAs(blob, filename+".csv");
}


//-------------
//BEST WAY TO LOAD FILE INTO JS
//XMLHttpRequest, i.e. AJAX, without the XML.

//create an XMLHttpRequest object, natively supported by browsers
let client = new XMLHttpRequest();
client.open('GET', 'src/data.csv'); //open(method,url,async,user,psw)	Specifies the request
client.onreadystatechange = function() {
    //Defines a function to be called when the readyState property changes
    alert(client.responseText); //Returns the response data as a string
};
client.send(); //Sends the request to the server, used for get requests
//--------------


//jquery init    #http://code.jquery.com/jquery-1.11.0.min.js
$(document).ready(function(){
//jquery code goes here

});


//load from csv
// <script src="src/data.csv" type="text/csv" id="unparsed">


//from https://stackoverflow.com/questions/42107492/json-stringify-es6-class-property-with-getter-setter
class MyClass {
  constructor(property) {
    this.property = property
  }

  set property(prop) {
  // Some validation etc.
  this._property = prop
  }

  get property() {
    return this._property
  }

  toJSON() {
    return {
      property: this.property
    }
  }
}

//----------------
//CRUD IMPLEMENT!! http://mrbool.com/creating-a-crud-form-with-html5-local-storage-and-json/26719
// REad from CSV -------- from https://stackoverflow.com/questions/7431268/how-to-read-data-from-csv-file-using-javascript
$(document).ready(function() {
    $.ajax({
        type: "GET",
        url: "data.txt",
        dataType: "text",
        success: function(data) {processData(data);}
     });
});

function processData(allText) {
    var allTextLines = allText.split(/\r\n|\n/);
    var headers = allTextLines[0].split(',');
    var lines = [];

    for (var i=1; i<allTextLines.length; i++) {
        var data = allTextLines[i].split(',');
        if (data.length == headers.length) {

            var tarr = [];
            for (var j=0; j<headers.length; j++) {
                tarr.push(headers[j]+":"+data[j]);
            }
            lines.push(tarr);
        }
    }
    // alert(lines);
}
//-----------------------

class GameBoard {
    constructor(width, height) {
        //constructs a 2d array of cells,
        this.width = width;
        this.height = height;
        this.gridmatrix = [];
        for ( let y = 0; y < height; y++ ) {
            this.gridmatrix[y] =[];
            for ( let x = 0; x < width; x++ ) {
                this.gridmatrix[y][x]= nceull;

            }
        }
        console.log(this.gridmatrix);
        return this;
    }
    getCell( x, y ) {
        let gridcell = this.gridmatrix[y][x];
        console.log(gridcell);
        return gridcell;
    }
    putCell( x, y, object) {
        this.gridmatrix[y][x] = object;
        let gridcell = this.gridmatrix[y][x];
        console.log(gridcell);
        return this;
    }
}


//keylogger
window.onkeyup = function(event) {
    let key = event.keyCode ? event.keyCode : event.which;
    logger.push(event.keyCode);
    console.log(`Event: ${event} Key: ${key}`);
    return key
};

function bindEventListener( element, event, action ) {
    //element: window, body, div etc.
    //event: load, click, keyup, keydown
    if (element.addEventListener){
        element.addEventListener(event, action, false);
        element.addEventListener(event, console.log(`Element: ${element} Event:${event} Action:${action}`));
        console.log(`${Event}listener bound to: ${element}`);
    }
    else if (element.attachEvent) {
        el.attachEvent('on' + event, action);
        console.log(`Event: ${event} action:${action} attached to:${element}`);
    }
}



//VARIABLES AND CONSTANTS
changeBackground("black");
changeColor("white");
buildGameBoard();