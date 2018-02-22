window.onload = function() {
    // buttons
    let quickAddBtn = document.getElementById("QuickAdd");
    let AddBtn = document.getElementById("Add");
    let cancelBtn = document.getElementById("Cancel");
    let quickAddFormDiv = document.querySelector('.quickAddForm');
    // can also documents.getElementsByClassName('quickAddFrom')[0]

    // bring in form fields

    let fullname = document.getElementById("fullname");
    let phone = document.getElementById("phone");
    let address = document.getElementById("address");
    let city = document.getElementById("city");
    let email = document.getElementById("email");

    // bring in the area we see our contents

    let addBookDiv = document.querySelector(".addbook");

    // Creating an array for storage

    let addressBook = [];

    // Create event listeners (getting events that occur)

    quickAddBtn.addEventListener("click", function(){
        quickAddFormDiv.style.display = "block";
    });

    cancelBtn.addEventListener("click", function () {
        quickAddFormDiv.style.display = "none";
    });

    AddBtn.addEventListener("click", addToBook);

    // using bubbling for the delete button/event

    addBookDiv.addEventListener("click", removeEntry);


 // this is a jason object. It will help us to "fill in" our form. Making variables inside the function.  No return needed. Automatically initializes as an object.
    function jsonStructure(fullname, phone, address, city, email){
        this.fullname = fullname;
        this.phone = phone;
        this.address = address;
        this.city = city;
        this.email = email;
    }

    // simplified validator. Create more regex validation checks later.
    function addToBook() {
        let isNull = fullname.value!= '' && phone.value!= '' && address.value!='' && city.value!='' && email.value!= "";
        if(isNull){
            // Add the contents of form to the array and local storage using the json object we created above (jsonStructure())
            let obj = new jsonStructure(fullname.value, phone.value, address.value, city.value, email.value);
            addressBook.push(obj); // Updates array  => pushes the object (our address book contents) into the array. Called a json array.
            localStorage['addbook'] = JSON.stringify(addressBook);   // localStorage is a database built into our browser. Can only store strings.
            // Hide the form panel
            quickAddFormDiv.style.display = "none";
            // clear form again
            clearForm();
            // Update and display all records in address book.
            showAddressBook();

        }

    }

    function removeEntry(event_object) {
        if(event_object.target.classList.contains("delbutton")) {  // checking where they are clicking /if it is on delete button
            let remID = event_object.target.getAttribute("data-id");
            // remove the JSON entry from array with the index number = remID
            addressBook.splice(remID, 1);
            localStorage = localStorage['addbook'] = JSON.stringify(addressBook);
            showAddressBook();

        }
     }

    function clearForm() {
        let frm = document.querySelectorAll(".formFields");
        for (let i in frm) {
            frm[i].value = '';
        }
    }

    function showAddressBook() {
        // check if the key 'addbook' exists in the localStorage, if not, create it. If it exists load contents from local storage and loop > display on page
        if(localStorage['addbook'] === undefined) {   // will return "undefined if it does not exists
            localStorage['addbook'] = "[]"; // storing an empty array as a string.
        } else {
            addressBook = JSON.parse(localStorage['addbook']);
            addBookDiv.innerHTML = '';
            for(let n in addressBook) {
                let str = '<div class="entry">';
                    str += '<table class="u-full-width">';
                    str += '<thead>';
                    str += '<tr>';
                    str += '<th> Name </th>';
                    str += '<th> Email </th>';
                    str += '<th> Phone </th>';
                    str += '<th> Address </th>';
                    str += '<th> City</th>';
                    str += '</tr>';
                    str += '<thead>';
                    str += '<tbody>';
                    str += '<tr>';
                    str += '<td class="name"><p>' + addressBook[n].fullname + '</p></td>';
                    str += '<td class="email"><p>' + addressBook[n].email + '</p></td>';
                    str += '<td class="phone"><p>' + addressBook[n].phone + '</p></td>';
                    str += '<td class="address"><p>' + addressBook[n].address + '</p></td>';
                    str += '<td class="city"><p>' + addressBook[n].city + '</p></td>';
                    str += '</tr>';
                    str += '<div class="del"><a href="#" class ="delbutton button" data-id="' + n + '"> Delete </a></div>';
                    str += '</tbody>';
                    str += '</table>';
                    str += '</div>';
                    addBookDiv.innerHTML += str;

            }
        }

    }

    showAddressBook();
};





