let btTimer = document.querySelector('#button-start');
let btStopTimer = document.querySelector('#button-stop');
let btResetTimer = document.querySelector('#button-reset');
let output = document.querySelector('#timer');


// make the clock tick
$(function() {
    function updateClock(){
        let now = moment(),
            second = now.seconds() * 6,
            minute = now.minutes() * 6 + second / 60,
            hour = (((now.hours()-3) % 12) / 12) * 360 + 90 + minute / 12;

        $('#hour').css("transform", "rotate(" + hour + "deg)");
        $('#minute').css("transform", "rotate(" + minute + "deg)");
        $('#second').css("transform", "rotate(" + second + "deg)");
    }

    function timedUpdate () {
        updateClock();
        setTimeout(timedUpdate, 1000);
    }

    timedUpdate();
});


// show the current time
setInterval(function () {
    let today = moment().format('MMMM Do YYYY, h:mm:ss a');
    let dateDisplay = document.querySelector('#date-display');
    dateDisplay.innerText = today;

}, 1000);

// countdown clock
let target_date = new Date("Apr 13, 2018").getTime();

// variables for time units
let days, hours, minutes, seconds;
let countdown = document.querySelector("#countdown");

// update the countdown every 1 second
setInterval(function () {

    // find the amount of "seconds" between now and target
    let current_date = new Date().getTime();
    let seconds_left = (target_date - current_date) / 1000;

    days = parseInt(seconds_left / 86400);
    seconds_left = seconds_left % 86400;

    hours = parseInt(seconds_left / 3600);
    seconds_left = seconds_left % 3600;

    minutes = parseInt(seconds_left / 60);
    seconds = parseInt(seconds_left % 60);

    // format countdown string + set tag value
    countdown.innerHTML = days + "d " + hours + "h "
    + minutes + "m " + seconds + "s ";

}, 1000);


btTimer.addEventListener('click', function() {
    console.log("start clicked");
    // make the timer appear
    $('#timer').toggleClass("hidden");
    $('#countdown').toggleClass("hidden");
    $('#timerh2').toggleClass("hidden");
    $('#countdownh2').toggleClass("hidden");
});

btStopTimer.addEventListener('click', function() {
    console.log("stop clicked");

});

btResetTimer.addEventListener('click', function() {
    console.log("stop clicked");
    // make the timer disappear
    $('#timer').toggleClass("hidden");
    $('#countdown').toggleClass("hidden");
    $('#timerh2').toggleClass("hidden");
    $('#countdownh2').toggleClass("hidden");
});



// Load when ready.
$( document ).ready(function() {
    console.log( "ready!" );
});

