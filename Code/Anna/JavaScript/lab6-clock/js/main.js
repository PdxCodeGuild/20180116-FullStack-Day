$(function() {
    function updateClock(){
        // moment.tz.setDefault("America/Los_Angeles");
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

let today = moment().format('MMMM Do YYYY, h:mm a');
let dateDisplay = document.querySelector('#date-display');
dateDisplay.innerText = today;


// Load when ready.
$( document ).ready(function() {
    console.log( "ready!" );


    // redirect
});


