// A $( document ).ready() block.
$( document ).ready(function() {
    console.log( "ready!" );
    $(".button-collapse").sideNav();
    $('.parallax').parallax();
});

$(function() {
  $('a.smooth-scroll[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: target.offset().top
        }, 1000);
        return false;
      }
    }
  });
});