

//declare HTML variables
const time_span = document.getElementById('time_span');
//click to copy date string to clipboard
const name_span = document.getElementById('name_span');


//formatting function
function format_digits(number) {
  //convert the number to a string
  let string_number = number.toString();
  //add a digit if necessary and return the number string
  return (string_number.length < 2)? '0' + string_number:
  string_number;
};


//setting up time and timeout update
// update interval in ms, 1000 is one second
function update_clock(update_interval) {

  //date variables
  let date = new Date();
  let year = date.getFullYear().toString();
  let month = (date.getMonth() + 1).toString();
  let day = date.getDate().toString();
  //day of current week
  let wk_day_i = date.getDay();
  let wk_days = 'NMTWRFS'; //idealized single letter day abbreviations
  let wk_day = wk_days[wk_day_i];
  //time
  let hour = (date.getHours()).toString();
  let minutes = date.getMinutes().toString();
  let seconds = date.getSeconds().toString();
  //format intervals to 2 digit strings
  month = format_digits(month);
  day = format_digits(day);
  hour = format_digits(hour);
  minutes = format_digits(minutes);
  seconds = format_digits(seconds);
  //update output
  time_span.innerHTML = `${year}.${month}.${day} ${wk_day}  ${hour}:${minutes}:${seconds}`;
  //Timeout callback function
  setTimeout(update_clock, update_interval);
};

//init and updaate clock
update_clock(1000);

//todo: copytext
//pulled from https://stackoverflow.com/questions/36639681/how-to-copy-text-from-a-div-to-clipboard
// function CopyToClipboard(containerid) {
// if (document.selection) {
//     let range = document.body.createTextRange();
//     range.moveToElementText(document.getElementById(containerid));
//     range.select().createTextRange();
//     document.execCommand("copy");

// } else if (window.getSelection) {
//     var range = document.createRange();
//      range.selectNode(document.getElementById(containerid));
//      window.getSelection().addRange(range);
//      document.execCommand("copy");
//      alert("text copied")
// }};

// name_span.onclick = function (event) {
//   let container = document.getElementById('container');
//   CopyToClipboard(container); };
//   let copy_
// = document.createElement('input')
//   copy_input.value = time_span.innerText;
//   // event.preventDefault(); //may not be necessary
//   // console.log(copy_input);
//   copy_input.select();
//   document.execCommand("Copy");
//   console.log(`copied: ${copy_input.value}`);
// };
//stopwatch
//TODO

//weather
//TODO

// function current_weather() {
//     if(navigator.geolocation){
//       navigator.geolocation.getCurrentPosition(function(position){
//         var lat = position.coords.latitude;
//         var long = position.coords.longitude;
//         showWeather(lat, long)
//       })
//     }
//        else {
//             window.alert("Could not get location");
//       }
//   }