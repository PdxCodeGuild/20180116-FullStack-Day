//CRUD DATABASE IN ES6 JS

//INITIAL HTML ELEMENTS
//define Title and Header Text
let title = 'CRUD JS ES6';
document.title = title; //update HTML
//set header
let header_text = 'A modular CRUD Database in JS ES6';
document.querySelector('header').innerText = header_text;

//main_div will be used to construct all elements
let main_div = document.querySelector('.main');
//create elements

//LOAD FILE TODO fix once working with server
function loadFile( source_path ) {
    //XMLHttpRequest, i.e. AJAX, without the XML.
    //create an XMLHttpRequest object, natively supported by browsers
    let client = new XMLHttpRequest();
    client.open('GET', source_path); //open(method,url,async,user,psw)	Specifies the request
    client.onreadystatechange = function () {
        //Defines a function to be called when the readyState property changes
        alert(client.responseText); //Returns the response data as a string
    };
    client.send(); //Sends the request to the server, used for get requests
}
// loadFile('src/data.csv');

class Table {
    constructor( headers, entries ) {
        // this.parent_container = parent_container;
        this.headers = headers;
        this.entries = entries;
        // this.append_empty_table();
        // this.append_header_row();

        // static append_empty_table
        // document.createElement('table', {className:'table'});
        let table = document.querySelector('.table'); //selector
        // main_div.appendChild(table);

        // append_header_row within table
        let header_row = document.createElement('tr');
        header_row.setAttribute('id', 'header_row');
        document.querySelector('.table').appendChild(header_row);
        //iterate through headers_fields create and fill a new column for each
        this.headers.forEach(function(field) {
            let curr_field = document.createElement('th');
            curr_field.innerText = field;
            header_row.appendChild(curr_field);
            });

        //iterate through entries,(create each row and fill with values)
        this.entries.forEach(function(entry) {
            //create the row container
            let curr_row = document.createElement('tr');
            curr_row.setAttribute('id', `${entry.id}`);
            table.appendChild(curr_row);
            console.log(entry);
            //create the fields for current row from entry values
            let curr_entry_values = Object.values(entry);
            console.log(curr_entry_values);
            // (headers.length === curr_entry_values.length)?
                curr_entry_values.forEach(function(val){
                let new_id = create_id();
                let entry_row_item = document.createElement('td');
                entry_row_item.innerText = val;
                entry_row_item.setAttribute('id', `${new_id}`);
                curr_row.appendChild(entry_row_item);
                });
                // : console.log(`header:value mismatch ${entry}`);

           });
        // create buttons
        let button_div = document.createElement('div');
        button_div.setAttribute('class', 'button_div');
        main_div.appendChild(button_div);
        let create_bt = this.button_creator(button_div, 'create_bt', CRUD.create_entry())
    }
    button_creator( parent, buttonid, onclick_function ) {
        let new_button = document.createElement('button');
        new_button.setAttribute('id', buttonid);
        new_button.innerText = buttonid;
        new_button.addEventListener('click', onclick_function);
        parent.appendChild(new_button);
        return new_button.id;
    }
    static remove_table() {
        document.querySelector('.table').remove();
    }

}

class Crud {
    //crud database holds entry_repository
    constructor(repository, fields) {
        this.entry_repository = repository || [];
        this.entry_fields = fields || [];
        // this.display_new_table()
    }

    //field methods
    get fields() {
        return this.entry_fields;
    }

    get_field_index(fieldname) {
        return this.entry_fields.indexOf(fieldname);
    }

    get_field_name(index) {
        return this.entry_fields[index]
    }

    add_new_field(fieldname) {
        this.entry_fields.push(fieldname);
        this.entry_repository.forEach(function (curr_entry) {
            curr_entry[fieldname] = null;
        }); //adds new field to each object
    }

    delete_field_index(index) {
        this.entry_fields.splice(index, 1);
        let curr_fieldname = this.get_field_name(index);
        this.entry_repository.forEach(function (curr_entry) {
            delete curr_entry[curr_fieldname];
        }); //deletes fields from entries
    }

    delete_field_name(fieldname) {
        let curr_index = this.get_field_index(fieldname);
        this.entry_fields.splice(curr_index, 1); //deletes fields
        this.entry_repository.forEach(function (curr_entry) {
            delete curr_entry[fieldname]; //deletes fields from entries
        })

    }
    //entry methods
    get entries() {
        return this.entry_repository;
    }

    create_entry() {
        let new_entry = {};
        this.fields.forEach(function(field) {
            new_entry[field] = null;
        });
        this.entry_repository.push(new_entry);
        this.update_table();
    }


    get_entry_by_index(item_index) {
        return this.entry_repository[item_index];
    }
    get_entry_values( entry ) {
        return this.Object.values(entry);
    }


    update_entry(item_index, updated_entry) {
        this.entry_repository[item_index] = updated_entry;
    }

    delete_entry(item_index) {
        this.entry_repository.splice(item_index, 1)
    }

    searchByProperties(key, value) {
        console.log('not currently supported');
        // for (let i = 0; i < this.entry_repository.length; i++) {
        //     if (this.entry_repository[i][key] === value) {
        //         return i;
        //     }
        //     return -1;  //if not found
        // }
    }

    // HTML METHODS
    update_table() {
        Table.remove_table();
        this.display_new_table()
    }
    display_new_table() {
        let headers = this.fields;
        let entries = this.entries;
        this.table = new Table(headers, entries);
    }
}


//test data
let test_entry = [{'name':'Bob', 'favorite color': 'blue', 'favorite fruit':'oatmeal'}];

let test_fields = ['name', 'favorite color', 'favorite fruit'];
let test_names = ['mort', 'morticia', 'morty', 'morgan'];
let test_colors = ['orange', 'fuscia', 'periwinkle', 'lavender'];
let test_fruits = ['persimmon', 'apples', 'lemons', 'tomatoes'];

//create test objects. iterate through test fields, append property.

function create_test_repository() {
    let test_repository = [];
    //iterate through
    for (let i=0; i<test_names.length; i++) {
        let new_object = {};
        new_object[test_fields[0]] = test_names[i];
        new_object[test_fields[1]] = test_colors[i];
        new_object[test_fields[2]] = test_fruits[i];
        test_repository.push(new_object);
    }
    return test_repository
}
let test_repo = create_test_repository();

// Instantiate repository
let CRUD = new Crud(test_repo, test_fields);
CRUD.display_new_table();

// Helper functions
function create_id() {
         return Math.random().toString(36).substr(2, 5) + (Date.now()).toString().join;
}



// Construct a table object into html




// user clicks create new entry button
//create a list with child fields
// inputs are shown based on how many items Key: input

//function called when user clicks create button
// function create_input_fields( crud_instance ) {
//     document.createElement('input')
//
// }


// to create a new entry: present user with fields based from crud.fields
        //this is crud.fields.length
        //this many user inputs will be generated.. elsewhere


// this will populate a list that the user can fill out, field[i] field[i++]
// for item in the length of that list, the user can fill in fields. click submit.
// submit will join fields to


// function create_new_entry( crud_instance ) {
//     curr_fields = crud_instance.fields; //get fields to present to user.
//     init_entry = {};
//     curr_fields.forEach(function(field) {
//         entry[field] = null;
//     });
//     //display the fields as values
//     //wait for inputs
// }





//     {id_list: 2, name: 'John', token: '123123'},
//     {id_list: 1, name: 'Nick', token: '312312'}
// ];

//crud database has entry_repository
//entry_repository

//crud contains entries. Entries have properties.
//entries get an ID when they are created,
//entries get an index when they are put into the database
//an entry knows its id so it can be called from a entry_repository
//entries properties can be extended

//an entry will be added to a entry_repository after all of its values are attained

//new properties are stored globally by the entry_repository in an array

//to append a new entry, all fields must be filled out.
//this field data is stored in a list
//the length of the list is determined by the global properties, stored by the database
//this is only updated when new properties are added
//for each property a user will be queried

//newEntry gets a blank property list to fill out

//update properties has to iterate through all objects and add null for field or they will be null when queried

//for property in properties, get value.
//object[properyvariablename] = value

//fill entry values .. return all values as a list. present that list to user as inputs.
//when user finishes filling, append new entry to entry_repository. give it an index and id.
