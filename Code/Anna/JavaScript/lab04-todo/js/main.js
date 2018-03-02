let plus = document.querySelector('#plus');

let edit_bt_text = '<i class="material-icons">edit</i>';
let save_bt_text = '<i class="material-icons">save</i>';
let delete_bt_text = '<i class="material-icons">delete_forever</i>';
let done_bt_text = '<i class="material-icons">done</i>';

let todo_input = document.querySelector('#todo_input');
let todo_table = document.querySelector('#todo_table');
let submit = document.querySelector('#todo_submit');


$(document).ready(function() {
    console.log("Ready!");

    plus.addEventListener('click', function() {
        $('#todo_input').removeClass('hidden-input');
        $('#todo_submit').removeClass('hidden-input');
        document.querySelector("#todo_input").focus();
    });

    submit.addEventListener('click', function() {
        let tr = document.createElement('tr');
        let td = document.createElement('td');
        let li_todo = document.createElement('li');
        let td_done = document.createElement('td');
        let td_edit = document.createElement('td');
        let td_save = document.createElement('td');
        let td_delete = document.createElement('td');
        li_todo.innerText = todo_input.value;

        // save the todo_item
        td_save.innerHTML = save_bt_text;
        td_save.classList.add('save_bt');
        td_save.style.display = 'none';
        td_save.onclick = function() {
            td_edit.style.display = 'initial';
            td_save.style.display = 'none';
            li_todo.setAttribute('contenteditable', 'false');
        };

        // edit the todo_item
        td_edit.innerHTML = edit_bt_text;
        td_edit.classList.add('edit_bt');
        td_edit.onclick = function() {
            td_edit.style.display = 'none';
            td_save.style.display = 'initial';
            li_todo.setAttribute('contenteditable', 'true');
        };

        // delete the todo_item
        td_delete.innerHTML = delete_bt_text;
        td_delete.classList.add('delete_bt');
        td_delete.onclick = function() {
            let tr = this.parentElement;
            let table = tr.parentElement;
            table.removeChild(tr);
        };

        // cross out the todo_item
        td_done.innerHTML = done_bt_text;
        td_done.classList.add('delete_bt');
        td_done.onclick = function() {
            li_todo.classList.toggle('strike');
        };

        todo_input.value = '';

        // put it all together
        tr.appendChild(td);
        td.appendChild(li_todo);
        tr.appendChild(td_done);
        tr.appendChild(td_edit);
        tr.appendChild(td_save);
        tr.appendChild(td_delete);

        todo_table.appendChild(tr);
    });

});
