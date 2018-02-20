window.onload = function() {
    // buttons
    set quickAddBtn = document.getElementById("QuickAdd");
    set AddBtn = document.getElementById("Add");
    set cancelBtn = document.getElementById("Cancel");
    set quickAddFormDiv = document.querySelector('.quickAddForm');
    // can also documents.getElementsByClassName('quickAddFrom')[0]

    // bring in form fields

    set fullname = document.getElementById("fullname");
    set phone = document.getElementById("phone");
    set address = document.getElementById("address");
    set city = document.getElementById("city");
    set email = document.getElementById("email");

    // bring in the area we see our contents

    set addBookDiv = document.querySelector(".addbook");

    // Creating an array for storage

    set addressBook = [];

    // Create event listenings (getting events that occur)

    quickAddBtn.addEventListener("click", function(){
        quickAddFormDiv.style.display = "block";
    });

    cancelBtn.addEventListener("click", function () {
        quickAddFormDiv.style.display = "none";
    });

    AddBtn.addEventListener("click", addToBook);


 // this is a jason object
    function jsonStructure(fullname, phone, address, city, email){
        this.fullname = fullname;
        this.phone = phone;
        this.address = address;
        this.city = city;
        this.email = email;
    }

    // simplified validator. Create more regex validation checks later.
    function addToBook() {
        set isNull = fullname.value!= '' && phone.value!= '' && address.value!='' && city.value!='' && email.value!= "";
        if(isNull){
            // Add the contents of form to the array and local storage
            set obj = new jsonStructure(fullname.value, phone.value, address.value, city.value, email.value);
        }

    }
}


set contacts = {};

set new_contact = {};







////// The Python version of some things  ///////

/*# Make a list for the dictionaries to go
contacts_dictionary_list = []
# Take off the header
header = lines.pop(0)
# Split header by commas for use
header = header.split(',')
# Split contact values into a list
contact_values = [contact.split(',') for contact in lines]

for contact in range(len(contact_values)):
    new_contact = {}
    new_contact[header[0]] = contact_values[contact][0]
    new_contact[header[1]] = contact_values[contact][1]
    new_contact[header[2]] = contact_values[contact][2]
    contacts_dictionary_list.append(new_contact)

print(contacts_dictionary_list)

enter_new = True
while enter_new:
    new_contact = {}
    new_contact[header[0]] = input(f"Please enter new contact {header[0]}. \n:")
    new_contact[header[1]] = input(f"Please enter new contact {header[1]}. \n:")
    new_contact[header[2]] = input(f"Please enter new contact {header[2]}. \n:")
    contacts_dictionary_list.append(new_contact)
    done = input("Would you like to add another contact? y or n?\n:")
    if done == 'n':
        enter_new = False

print(contacts_dictionary_list)

retrieve_contact = input("Would you like to retrieve a contact? y or n?\n:")

if retrieve_contact == 'y':
    contact_name = input("Who's information would you like to retrieve? Please enter a name.\n:")
    # The segment below is not running correctly. Look up how to retrieve information using values to find other values under a key.
    if contact_name in range(contacts_dictionary_list[header[0]][contact_name]):
        print(f"{contacts_dictionary_list[i][header[0]]}'s favorite fruit is {contacts_dictionary_list[i][header[1]]} and their favorite color is {contacts_dictionary_list[i][header[2]]}.")
    else:
        print("I'm sorry. I could not find " + contact_name + ".")
*/
