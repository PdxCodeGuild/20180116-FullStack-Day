


function updateTime() {

    let time = new Date();
    let hours = time.getHours();
    let minutes = time.getMinutes();
    let seconds = time.getSeconds();
    let amPm = "AM";

    if (hours === 0){
        hours = 12;
    }

    hours = (hours < 10)? "0" + hours : hours;
    minutes = (minutes < 10)? "0" + minutes : minutes;
    seconds = (seconds < 10)? "0" + seconds : seconds;

    if (hours > 12){
        hours = hours - 12;
        amPm = "PM";
    }

    let timed = hours + ':' + minutes + ':' + seconds + ' ' + amPm;

    document.querySelector('#clockedIn').innerHTML = timed;
}

setInterval(updateTime, 1000);
