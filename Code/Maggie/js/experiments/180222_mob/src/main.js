
//HTML ELEMENTS
//define Title and Header Text
let title = 'Test File';
document.title = title;
let header_text = 'A simple CRUD Database in JS';

//Selector variables
// let main_div = document.getElementById('main'); //contains all other divs
let header_div = document.getElementById('header');
let data_div = document.getElementById('data_container');
let message_div = document.getElementById('message_container');
let button_div = document.getElementById('button_container');

//create HTML Elements, Append to parent elements.
//helper function for creating elements
function appendNewElement(parent, type, innertext, id) {
    let new_element = document.createElement(type);
    console.log(`${type} created!`);
    new_element.id = id || null;
    new_element.innerText = innertext || null;
    parent.appendChild(new_element);
    console.log(`created element: ${type}. parent: ${parent}. id: ${id}.`);
}

//Set header
header_div.innerText = header_text;

//MAIN DISPLAY TEXT: message_div
appendNewElement(data_div, 'textarea', '', 'data_text');
let message_div = document.getElementById('data_text');
//settings
message_div.rows = 20;
message_div.cols = 100;
message_div.wrap;
message_div.style.fontSize = "large";
message_div.readOnly = true;

//DISPLAY UPDATERS
let data_array = [];

//clears data array message buffer and text area
function clear_display_text() {
    data_array = [];
    message_div.value = '';
}

function append_display_text(message) {
    data_array.push(message);
    message_div.value = '';
    for (let i=0; i < data_array.length; i++) {
        message_div.value += data_array[i];
    }
    // return this;
}

//Data area sample text area
let line_one = 'To load the database into the program: \n';
let line_two = '1. From the terminal, type python3 -m http.server; \n';
let line_three = '2. navigate to the html file directory';
// load_text = line_one + line_two + line_3;
append_display_text(line_one);
append_display_text(line_two);
append_display_text(line_three);

//create buttons
appendNewElement(button_div, 'ul', 'Options', 'button_ul');
const button_ul = document.getElementById('button_ul');
appendNewElement(button_ul, 'button', 'Load Database', 'load');
const load_button = document.getElementById('load');
appendNewElement(button_ul, 'button', 'New Entry', 'create');
appendNewElement(button_ul, 'button', 'List Entries', 'list_entries' );
appendNewElement(button_ul, 'button', 'New Entry', 'create');
appendNewElement(button_ul, 'button', 'Edit Existing Entry', 'edit');
appendNewElement(button_ul, 'button', 'Save Data', 'Save to File');

//input area = message container
appendNewElement(message_div, 'input', null, 'main_input');
appendNewElement(message_div, 'button', 'enter', 'enter');
appendNewElement(message_div, 'span', 'Status Messages', 'status_text');
status_text = document.getElementById('status_text');
main_input = document.getElementById('main_input');


//LOAD FILE FUNCTION
function loadFile( source_path) {
    console.log(`Attempting to load from ${source_path}`);

    //XMLHttpRequest, i.e. AJAX, without the XML. XMLHttpRequest object, natively supported by most browsers.
    let client = new XMLHttpRequest();
    client.open('GET', source_path); //open(method,url,async,user,psw)	Specifies the request
    client.onreadystatechange = function(data) {  //Defines a function to be called when the readyState property changes
            // if(client.readyState === XMLHttpRequest.DONE && client.status === 200) {
            alert(data);
            console.log(data);
            alert(client.responseText);
            // if (client.status == 200) {
            //     let response_text = client.responseText;
            //     console.log(response_text);
            //     alert(response_text);
            //     return response_text;
            // }
            // return response_text
        };
        // client.send(); //Sends the request to the server, used for get requests


//LOAD FILE DATA INTO OBJECTS
// let crud_object_array = [];  //init array
// function processData(raw_csv_data) {
//     let text_lines = raw_csv_data.split('\n');
//     let headers = text_lines[0].split(',');
//     let result_array = [];
//
//     // create objects
//     for (let i=1; i<text_lines.length; i++) {
//         let line_object = {};
//         let current_line = text_lines[i].split(',');
//         let data = text_lines[i].split(',');
//         for (let j=0; j < headers.length; j++) {
//                 line_object[headers[j]] = current_line[j];
//         } result_array.push(line_object);
//     }
//     // alert(result_array);
//     return JSON.stringify( result_array )
// }

//HELPER FUNCTION TO PROCESS FILE DATA
// let file_path = 'src/data.csv';
// function load_and_process( file_path ) {
//     let raw_text = loadFile( file_path );
    // crud_object_array = processData(raw_text);
    // clear_display_text();
    // append_display_text(`file data loaded. loaded: ${crud_object_array.length + 1} objects` );
    // append_display_text(raw_text)
    // append_display_text(raw_text); //put it directly

}
//LOAD BUTTON FUNCTIONALITY
load_button.addEventListener("click", function () {load_and_process( file_path )} );



// function createPageElement(parent_element, element_type, element_class, element_id) {
//     //create the container and its children: header, input box, button
//
//     element.className = element_class || null;
//
//     document.querySelector(parent_element).appendChild(element);
// }


// //create elements
// createPageElement('.main', 'div', 'textDisplayBox', 'textDisplayBox', 'testing');
// createPageElement('.main', 'input', 'mainInput', 'mainInput');
// createPageElement('.main', 'button', 'button', 'button', 'hello');
// document.querySelector('#mainInput').placeholder = 'input text here';
// document.querySelector("#textDisplayBox").innerHTML = loadUrl();




// let csv = document.querySelector("#unparsed").innerHTML;

// $(document).ready(function() {
//
// });
//
// function processData(allText) {
//     var allTextLines = allText.split(/\r\n|\n/);
//     var headers = allTextLines[0].split(',');
//     var lines = [];
//
//     for (var i=1; i<allTextLines.length; i++) {
//         var data = allTextLines[i].split(',');
//         if (data.length === headers.length) {
//
//             var tarr = [];
//             for (var j=0; j<headers.length; j++) {
//                 tarr.push(headers[j]+":"+data[j]);
//             }
//             lines.push(tarr);
//             console.log(tarr)
//         }
//     }
//     // alert(lines);
// }

// var urls = ["src/data.csv"];
//
// function loadUrl() {
//     var urlToLoad = urls[0];
//     alert("load URL ... " + urlToLoad);
//     browser.setAttributeNS(xlinkNS, "href", urlToLoad);
//
//
// }



//jquery init    #http://code.jquery.com/jquery-1.11.0.min.js
// $(document).ready(function(){
//
//
// $.ajax({
//     type: "GET",
//     url: "src/data.csv",
//     dataType: "text",
//     success: function(data) {processData(data);}
//
//  ajax();
//  });





// let dataSet =	$(function parseData(){
// 			    $("#file").hide();
// 		    	let data = $("#unparsed").html();
// 		    	var parsed = $.parse(data);
// 		    	$("#parsed").val(JSON.stringify(parsed));
// });



// }); //end of jquery function

// let test_array = [["name1", 2, 3], ["name2", 4, 5], ["name3", 6, 7], ["name4", 8, 9], ["name5", 10, 11]];






// saveArrayToCSV(test_array, 'text');
