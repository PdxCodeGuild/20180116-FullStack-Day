

set('hours',   30 * new Date().getHours());
set('minutes',  6 * new Date().getMinutes());
set('seconds', 10 * new Date().getSeconds());

function set(id, degrees) {
  let el = document.getElementById(id),
      rotation = 'rotate(' + degrees + 'deg)';

  el.style.transform = rotation;
  el.style.webkitTransform = rotation;
}







/*let stop_time_bt = document.getElementById('#stop_time_bt')
let MyClock = setInterval(myTimer, 1000);

function myTimer() {
    let d = new Date();
    document.getElementById("clock").innerHTML = d.toLocaleTimeString();
}


function stop_time(button, variable) {
    .onclick = clearInterval(variable);
}

stop_time(stop_time_bt, MyClock); */
