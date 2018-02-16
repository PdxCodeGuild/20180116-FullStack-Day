// this makes the fancy pop-up footer work
jQuery(function($) {
	var open = false;
	$('#footerSlideButton').click(function () {
		if(open === false) {
			if(Modernizr.csstransitions) {
				$('#footerSlideContent').addClass('open');
			} else {
				$('#footerSlideContent').animate({ height: '300px' });
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


function generator() {
    let randomEyes = eyes[Math.floor(Math.random() * eyes.length)];
    let randomNose = noses[Math.floor(Math.random() * noses.length)];
    let randomMouth = mouths[Math.floor(Math.random() * mouths.length)];

    let eyeOutput = document.querySelector('#eye');
    let noseOutput = document.querySelector('#nose');
    let mouthOutput = document.querySelector('#mouth');

    eyeOutput.innerText = randomEyes;
    noseOutput.innerText = randomNose;
    mouthOutput.innerText = randomMouth;
}





