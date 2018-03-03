
// drawing
let canvas = document.getElementById("canvas"),
		ctx = canvas.getContext("2d");

let canvas.height =

let ball = {
    radius: 4,
    px: Math.random()*width,
    py: Math.random()*height,
    vx: (2*Math.random()-1)*10,
    vy: (2*Math.random()-1)*10
};


ctx.beginPath();
ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
ctx.fillStyle = 'pink';
ctx.fill();

function main_loop() {
    // update the ball's position
    this.vx -= (this.vx)*2;
    this.vy += (this.vy)*2;
    // check if it hit a boundary
    if (this.vx <= 0) {

    }
    // draw the ball
    window.requestAnimationFrame(main_loop);
}
window.requestAnimationFrame(main_loop);