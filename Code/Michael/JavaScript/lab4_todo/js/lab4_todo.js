



window.onload = function() {

    let listA = document.getElementById("listA");
    let listB = document.getElementById("listB");

    let todo = document.getElementById('todo');
    let add_bt = document.getElementById('add_bt');
    let remove_bt = document.getElementById('remove_bt');

    console.log(todo);

    add_bt.onclick = function() {
      let li = document.createElement("li");
      li.innerText = todo.value;
      listA.appendChild(li);
    };

    remove_btA.onclick = function() {
      //let item = document.getElementById(todo.value);
      listA.removeChild(listA.firstChild);
    };

    complete_bt.onclick = function() {
      let li = document.createElement("li");
      li.innerText = complete.value;
      listB.appendChild(li);
    };

    remove_btB.onclick = function() {
      //let item = document.getElementById(todo.value);
      listB.removeChild(listB.firstChild);
    };



}