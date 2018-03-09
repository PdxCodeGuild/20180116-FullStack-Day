let add_bt = document.getElementById('add_bt');
let u_input = document.getElementById('user_input')
let list = document.querySelector('ul')

  //ADD BUTTON CLICK
add_bt.onclick = function() {
  if (u_input.value === '') {
    return alert('enter a task')
  }
  //create new elements
  let li = document.createElement('li');
  let span = document.createElement('span');
  let delete_bt = document.createElement('button');

  //
  delete_bt.className = 'delete'

  //set inner text
  span.innerText = u_input.value;
  u_input.value = '';
  // complete_bt.innerText = "✓";
  delete_bt.innerText = "✕";

  //Delete BUTTON CLICK
  delete_bt.onclick = function() {
    let li = this.parentElement;
    let ul = li.parentElement;
    list.removeChild(li);
  };
  ////COMPLETE list Item CLICK
  li.onclick = function(event) {
    event.target.classList.toggle('checked')
  };

  // complete_bt.style.color = "rgb(166,226,46)";
  delete_bt.style.color = "rgb(249,38,114)";


  li.appendChild(span);
  // li.appendChild(complete_bt);
  li.appendChild(delete_bt);

  list.appendChild(li);
};


