// A $( document ).ready() block.
"use strict";

$( document ).ready(function() {
    console.log( "ready!" );
    $('.collapsible').collapsible();
    $(".button-collapse").sideNav();
    $('.parallax').parallax();
    $('.modal').modal();
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


// AFFIX LOWER NAVBAR ON SCROLL
$(window).scroll(function() {
    var scroll = $(window).scrollTop();
    if (scroll >= 284) {
        $(".navbar-lower").addClass("navbar-fixed");
    }
    else {
        $(".navbar-lower").removeClass("navbar-fixed");
    }
});