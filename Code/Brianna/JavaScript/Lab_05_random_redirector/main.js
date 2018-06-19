

let website_array = ["https://www.booooooom.com/", "https://www.brainpickings.org/", "https://laughingsquid.com/", "http://www.theuselessweb.com/",
"http://theoatmeal.com/", "http://explosm.net/", "https://hyperboleandahalf.blogspot.com/", "https://omgfacts.com/", "http://www.staggeringbeauty.com/", "http://paperjs.org/about/", "http://tholman.com/texter/",
"http://thequietplaceproject.com/", "http://www.rainymood.com/", "http://www.fallingfalling.com/", "http://eelslap.com/", "http://lolmythesis.com/", "http://world.time.com/timelapse/", "https://www.whoishostingthis.com/",
"https://www.midomi.com/", "https://www.myfonts.com/WhatTheFont/", "http://e.ggtimer.com/", "https://www.isitnormal.com/", "http://textastrophe.com/", "http://www.whatshouldireadnext.com/index.php", "https://www.brainpickings.org/",
"https://www.wolframalpha.com/", "http://myfridgefood.com/", "https://cvmkr.com/", "https://www.whoishostingthis.com/", "http://cffjh.relaxkitten.win/lp/fb8b2497/?n=371286185", "http://www.rainymood.com/", "http://tholman.com/texter/",
"http://www.fallingfalling.com/", "http://schillmania.com/projects/soundmanager2/", "https://www.random.org/"];
let arrayLength = website_array.length;
let random_index = Math.floor(Math.random() * arrayLength);
let go_to_a_website_bt = document.querySelector('#go_to_a_website');
let output_span = document.querySelector('#output_span');
let counter = 5;


go_to_a_website_bt.onclick = function () {
    setTimeout(function () {
        location = website_array[random_index];
    }, 5000);
};

//
// while (counter >0) {
//     setInterval(function() {
//     output_span.innerText = counter;
//    counter -= 1;
//  }, 1000);
// }
//




/* locations to go:

https://www.booooooom.com/

https://www.wolframalpha.com/

http://www.whatshouldireadnext.com/index.php

http://l-mail.com/

https://www.brainpickings.org/

 http://schillmania.com/projects/soundmanager2/

https://laughingsquid.com/

http://www.theuselessweb.com/

http://myfridgefood.com/

https://cvmkr.com/

https://www.cheatography.com/

http://passwordsgenerator.net/

https://www.calculator.com/

http://theoatmeal.com/

http://explosm.net/

https://hyperboleandahalf.blogspot.com/

https://omgfacts.com/

http://textastrophe.com/

https://www.isitnormal.com/

https://dictation.io/

http://e.ggtimer.com/

https://www.random.org/

http://scr.im/

https://www.myfonts.com/WhatTheFont/

https://www.homestyler.com/

http://everytimezone.com/

https://www.midomi.com/

https://www.whoishostingthis.com/

http://world.time.com/timelapse/

http://lolmythesis.com/

http://eelslap.com/

http://www.pointerpointer.com/
http://cffjh.relaxkitten.win/lp/fb8b2497/?n=371286185

http://www.fallingfalling.com/

http://www.rainymood.com/

http://thequietplaceproject.com/

http://tholman.com/texter/


*/