

let website_array = ["https://www.booooooom.com/", "https://www.brainpickings.org/", "https://laughingsquid.com/", "http://www.theuselessweb.com/",
"http://theoatmeal.com/", "http://explosm.net/", "https://hyperboleandahalf.blogspot.com/", "https://omgfacts.com/", "http://www.staggeringbeauty.com/", "http://paperjs.org/about/"];
let arrayLength = website_array.length;
alert(arrayLength);
let random_index = Math.floor(Math.random() * arrayLength);
let go_to_a_website_bt = document.querySelector('#go_to_a_website');

alert(random_index);
go_to_a_website_bt.onclick = function () {
    location = website_array[random_index];
};



/* locations to go:

https://www.booooooom.com/

https://www.brainpickings.org/

 http://schillmania.com/projects/soundmanager2/

https://laughingsquid.com/

http://www.theuselessweb.com/

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