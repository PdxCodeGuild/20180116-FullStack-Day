//identifying variables
let output_span = document.querySelector("#output_span");
let start_stop_bt = document.querySelector("#start_stop_bt");
let reset_bt = document.querySelector("#reset_bt");
let lap_bt = document.querySelector("#lap_bt");
let running = false;
let lap_list = document.querySelector("#lap_list");
//counters
let counter = 0;
let laps = 0;

//resets the counter and clears/removes laps
reset_bt.onclick = function() {
  counter = 0;
  laps = 0
  clear_laps()
};

//start stop changes playing state
start_stop_bt.onclick = function() {
  running = running ? false : true;
  start_stop_bt.innerText = running ? "stop" : "start";
};

//increment counter if running is true
function increment_check() {
  if (running) {
    counter += 1;
  } else {
    start_stop_bt.innerText = "start";
    clearInterval();
  }
  output_span.innerText = counter_format(counter);
}

//formatting function
function format_digits(number) {
  //convert the number to a string
  let string_number = number.toString();
  //add a digit if necessary and return the number string
  return string_number.length < 2 ? "0" + string_number : string_number;
}

function counter_format(counter) {
  //parsing counter into time
  let deciseconds = counter % 10;
  let seconds = Math.floor((counter / 10) % 60);
  let minutes = Math.floor((counter / 600) % 60);
  let hours = Math.floor(counter / 600 / 60);

  //formatting digits
  seconds = format_digits(seconds);
  minutes = format_digits(minutes);
  hours = format_digits(hours);
  //putting it together
  let formatted_time = `${hours}:${minutes}:${seconds}:${deciseconds}`;
  // console.log(formatted_time);
  return formatted_time;
}
// start the interval callback
setInterval(function() {
  increment_check();
}, 100);

// lap function
function new_lap() {
  if (counter > 0) {
    let curr_lap = counter_format(counter);
    let li = document.createElement('li');
    laps++
    li.innerText = `Lap ${laps}: ${curr_lap}`;
    lap_list.appendChild(li);
  }
}

function clear_laps() {
    while (lap_list.firstChild) {
    lap_list.removeChild(lap_list.firstChild);
}
};

lap_bt.onclick = function () {
    new_lap();
};