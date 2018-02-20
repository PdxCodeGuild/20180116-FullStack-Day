// this makes the fancy pop-up footer work
jQuery(function($) {
	var open = false;
	$('#footerSlideButton').click(function () {
		if(open === false) {
			if(Modernizr.csstransitions) {
				$('#footerSlideContent').addClass('open');
			} else {
				$('#footerSlideContent').animate({ height: '30vh' });
			}
			$(this).css('backgroundPosition', 'bottom left');
			open = true;
		} else {
			if(Modernizr.csstransitions) {
				$('#footerSlideContent').removeClass('open');
			} else {
				$('#footerSlideContent').animate({ height: '0px' });
			}
			$(this).css('backgroundPosition', 'top left');
			open = false;
		}
	});
});


// this was so much easier in python

let eyes = [':', ':', '=', '<:', '>:', '[:', '{:', 'X', 'O;']
let noses = ['-', '>', '^', '=', '~', '', '-']
let mouths = ['O', '0', 'o', ')', '(', ']', '}', '%', '#', '@', '*', '|', 'D', 'P']
let happy = [')', ']', '}', '*', 'D', 'P']
let sad = ['(', '[', '{', '(', '<']
let meh = ['O', '0', 'o', '%', '#', '@', '*', '|']
let rotated = false;
let mood_input = document.querySelector('#mood_input');
let mood = mood_input.value;


// start the animations

$(document).ready(function() {
    console.log("ready!");
    $('#clicker').click(function() {
        let randomEyes = eyes[Math.floor(Math.random() * eyes.length)];
        let randomNose = noses[Math.floor(Math.random() * noses.length)];
        let randomHappy = happy[Math.floor(Math.random() * happy.length)];
        let randomSad = sad[Math.floor(Math.random() * sad.length)];
        let randomMeh = meh[Math.floor(Math.random() * meh.length)];

        let eyeOutput = document.querySelector('#eye');
        let noseOutput = document.querySelector('#nose');
        let mouthOutput = document.querySelector('#mouth');

        eyeOutput.innerText = randomEyes;
        noseOutput.innerText = randomNose;

        if (mood === "happy" || mood === "good") {
            mouthOutput.innerText = randomHappy;
        }
        else if (mood === "sad" || mood === "bad") {
            mouthOutput.innerText = randomSad;
        }
        else  {
            mouthOutput.innerText = randomMeh;
        }


        // document.getElementById('generator_div').className = 'animate';

        $('#rotating').toggleClass('rotated');
        console.log("I should be done now.");
    });
    $('#more').on('click', function(){
        for (let i=1; i<11; ++i) {
            let element = document.querySelector('.x'+i);
            element.style.AnimationPlayState = "running";
            element.style.webkitAnimationPlayState = "running";
        }
        console.log("started the floating emojis");
    });
});


