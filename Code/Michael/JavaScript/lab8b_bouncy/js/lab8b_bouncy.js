let canvas = document.getElementById('canvas');
let context = canvas.getContext('2d');
 
let g = 0.1;
let fac = 0.8;
let radius = 20;
let color = "#0000ff";
 
let x = 50;
let y = 50;
let vx = 2;
let vy = 0;
 
window.onload = init;
 
function init() {
    setInterval(update, 1000/60);
}
 
function update() {
  vy += g;
 
  x += vx;
  y += vy; 
 
  if (y > canvas.height - radius){
    y = canvas.height - radius;
    vy *= -fac;
  }
 
  if (x > canvas.width + radius){
    x = -radius;
  }
 
  drawBall();
}
 
function drawBall() {
    with (context){
        clearRect(0, 0, canvas.width, canvas.height);
        fillStyle = color;
        beginPath();
        arc(x, y, radius, 0, 2*Math.PI, true);
        closePath();
        fill();
    }
}