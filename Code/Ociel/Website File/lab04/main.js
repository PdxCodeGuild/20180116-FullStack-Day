// This is the code needed to print and fade out in the begining
// of the page. I had to download typed.js and work with that.

let typed = new Typed(".type", {
  strings: ["build websites.", "work with start ups.",
            "help you start your entrepreneurial journey.",
            "make it home on time!"],
    typeSpeed: 60,
    fadeOut:true,
    loop: true
});


// When the navigation bar is clicked.
let toggle_btn = document.querySelector('.toggle-btn');
toggle_btn.onclick = function () {
    document.getElementById('sidebar').classList.toggle('active');
};