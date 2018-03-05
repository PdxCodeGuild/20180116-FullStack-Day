let canvas = document.getElementById('cnv');
let ctx = canvas.getContext('2d');
let height = window.innerHeight;
let ratio = canvas.width/canvas.height;
let width = height * ratio;
let raf;
let running = false;
let start = document.querySelector('#bt-start');
let stop = document.querySelector('#bt-stop');
let reset = document.querySelector('#bt-reset');

// make musics!
//create a synth and connect it to the master output
let pingPong = new Tone.PingPongDelay("4n", 0.2).toMaster(); // add ping-pong delay on one synth
let wallSynth1 = new Tone.DuoSynth().connect(pingPong);
let wallSynth2 = new Tone.DuoSynth().toMaster();

// for the musics
// noteArray = ['C#4', 'D4', 'E4', 'F#4', 'G#4', 'A#4', 'B4', 'C#5', 'C#3', 'D3', 'E3', 'F#3', 'G#3', 'A#3', 'B3', 'A#2', 'A#5', 'D5', 'F#5'];
noteArray = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'A2', 'A5', 'D5', 'F5'];

// define the Ball class
class Ball {
	constructor() {
		this.x = Math.random()*width;
		this.y = Math.random()*height;
		this.vx = (2*Math.random()-1)*10;
		this.vy = (2*Math.random()-1)*10;
		this.radius = ((5*Math.random()-1)*10)+10;
		this.color = '#'+Math.random().toString(16).substr(-6);
	}
	draw(ctx) {
		ctx.beginPath();
		ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2, true);
		ctx.closePath();
		ctx.fillStyle = this.color;
		ctx.fill();
  }
}

// kinda clear the canvas
function clear() {
	ctx.fillStyle = 'rgba(23, 16, 54, 0.3)';
	ctx.fillRect(0, 0, canvas.width, canvas.height);
}

// resets the canvas
function allClear() {
	ctx.clearRect(0,0, canvas.width, canvas.height);
	makeBalls();
}

// make more balls!
function makeBalls() {
    let balls = [];
    for (let i=0; i<10; ++i) {
        let ball = new Ball();
        balls.push(ball);
    }
    return balls;
}
let balls = makeBalls();

// make all the balls move
function move() {
	clear();
	// draw the balls that were made
	for (let i=0; i<10; ++i) {
		balls[i].draw(ctx);
		// move the balls
		balls[i].x += balls[i].vx;
		balls[i].y += balls[i].vy;
		balls[i].vy *= 1.000000000001;
		balls[i].vy += .25;

		let note1 = noteArray[Math.floor(Math.random() * noteArray.length)];
		let note2 = noteArray[Math.floor(Math.random() * noteArray.length)];

		// bounce off the walls and make pretty sounds
		if (balls[i].y + balls[i].vy > canvas.height || balls[i].y + balls[i].vy < 0) {
			balls[i].vy = -balls[i].vy;
			wallSynth1.triggerAttackRelease(note1, '8n');
		}
		if (balls[i].x + balls[i].vx > canvas.width || balls[i].x + balls[i].vx < 0) {
			balls[i].vx = -balls[i].vx;
			wallSynth2.triggerAttackRelease(note2, '8n');
		}
	}
	raf = window.requestAnimationFrame(move);
}

start.addEventListener('click', function() {
    console.log('starting animation');
    if (!running) {
        raf = window.requestAnimationFrame(move);
        running = true;
    }
});

stop.addEventListener('click', function() {
    console.log('stopping animation');
    window.cancelAnimationFrame(raf);
    running = false;
});

reset.addEventListener('click', function() {
    console.log('resetting animation');
    allClear();
    window.cancelAnimationFrame(raf);
    running = false;
    balls = makeBalls();
});


// makes the canvas responsive. Yay!
function resize() {
	// Our canvas must cover full height of screen
	// regardless of the resolution
	let height = window.innerHeight;

	// So we need to calculate the proper scaled width
	// that should work well with every resolution
	let ratio = canvas.width/canvas.height;
	let width = height * ratio;

	canvas.width = width;
	canvas.height = height;
}

window.addEventListener('load', resize, false);
window.addEventListener('resize', resize, false);
