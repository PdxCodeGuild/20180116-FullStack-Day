// declare all the things
let buttonStart = document.querySelector('#button-start');
let buttonStop = document.querySelector('#button-stop');
let buttonReset = document.querySelector('#button-reset');
let appendTens = document.querySelector("#tens");
let appendSeconds = document.querySelector("#seconds");
let tm_seconds = '00';
let tm_tens = '00';
let Interval ;

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


buttonStart.addEventListener('click', function() {
    console.log("start clicked");
    // make the timer appear
    $('#timer').toggleClass("hidden");
    $('#countdown').toggleClass("hidden");
    $('#timerh2').toggleClass("hidden");
    $('#countdownh2').toggleClass("hidden");
    clearInterval(Interval);
    Interval = setInterval(startTimer, 10);
});

buttonStop.addEventListener('click', function() {
    console.log("stop clicked");
    clearInterval(Interval);
});

buttonReset.addEventListener('click', function() {
    console.log("stop clicked");
    // make the timer disappear
    $('#timer').toggleClass("hidden");
    $('#countdown').toggleClass("hidden");
    $('#timerh2').toggleClass("hidden");
    $('#countdownh2').toggleClass("hidden");
    clearInterval(Interval);
    tm_tens = "00";
    tm_seconds = "00";
    appendTens.innerHTML = tm_tens;
    appendSeconds.innerHTML = seconds;
});


function startTimer () {
    tm_tens++;
    if (tm_tens < 9) {
        appendTens.innerHTML = "0" + tm_tens;
    }
    if (tm_tens > 9) {
        appendTens.innerHTML = tm_tens;
    }
    if (tm_tens > 99) {
        console.log("seconds");
        tm_seconds++;
        appendSeconds.innerHTML = "0" + tm_seconds;
        tm_tens = 0;
        appendTens.innerHTML = "0" + 0;
    }
    if (tm_seconds > 9) {
        appendSeconds.innerHTML = tm_seconds;
    }
}

