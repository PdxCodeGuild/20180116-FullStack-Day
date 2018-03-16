let canvas = document.getElementById('canvas'); // get the canvas
let context = canvas.getContext('2d'); // specify whether it is 2d or 3d?


class Balls {
    constructor() {
        this.xPosition = Math.random() * canvas.width;
        this.yPosition = Math.random() * canvas.height;
        this.xVelocity = (2 * Math.random() - 1) * 10; // x movement increment per framerate. Keeping this standard for now
        this.yVelocity = (2 * Math.random() - 1) * 10; // y movement increment per framerate
        this.gravity = .8; // Let's bounce on the moon!
		this.damping = .99; // The effect of the moon is extra bounce-ability
        this.friction = .99; // Unfortunately friction is a tough thing
        this.radius = ((5 * Math.random() - 1) * 10) + 10;
        this.color = '#42c5f4';
    }

    draw(context) {  // start drawing our balls.
        context.beginPath(); // start of our path
        context.arc(this.xPosition, this.yPosition, this.radius, 0, Math.PI * 2, true); // our arc/how they change
        context.closePath(); // end of our path
        context.fillStyle = this.color;  // whatever color we give them
        context.fill(); // filling them up with color... if we decide to.
    }
}
// Make some balls
function makingBalls() {
    let balls = [];
    for (let i=0; i<5; ++i) {
        let ball = new Balls();
        balls.push(ball);
    }
    return balls;
}
let balls = makingBalls();


function mainLoop() {
	context.clearRect(0, 0, canvas.width, canvas.height); // clear frame every redraw
	// Draw all balls we have created
	for (let i=0; i<5; ++i) {
		balls[i].draw(context);
		// mainLoop the balls with gravity and friction
		balls[i].xPosition += balls[i].xVelocity; // add movement increment to position x
		balls[i].yPosition += balls[i].yVelocity; // add movement increment to position y
		// Create left and right wall bounce functionality
		if (balls[i].xPosition + balls[i].radius >=canvas.width) {
			balls[i].xVelocity = -balls[i].xVelocity * balls[i].damping;
			balls[i].xPosition = canvas.width - balls[i].radius;
		} else if (balls[i].xPosition - balls[i].radius <=0) {
			balls[i].xVelocity = -balls[i].xVelocity * balls[i].damping;
			balls[i].xPosition = balls[i].radius;

		} // now create top and bottom bounce! ^_^
		if (balls[i].yPosition + balls[i].radius > canvas.height){
			balls[i].yVelocity = - balls[i].yVelocity *balls[i].damping;
			balls[i].yPosition = canvas.height - balls[i].radius;
			balls[i].xVelocity *= balls[i].friction;
		} else if (balls[i].yPosition - balls[i].radius <= 0) {
            balls[i].yVelocity = -balls[i].yVelocity * balls[i].damping;
            balls[i].yPosition = balls[i].radius;
        }
        balls[i].yVelocity += balls[i].gravity; // Always applying gravity through the y axis
		balls[i].yPosition += balls[i].yVelocity; // adjust the position of x for the movement of x
		balls[i].xPosition += balls[i].xVelocity; // adjust the position of y for the movement of y

	 }
        window.requestAnimationFrame(mainLoop);
    }

    window.requestAnimationFrame(mainLoop);


