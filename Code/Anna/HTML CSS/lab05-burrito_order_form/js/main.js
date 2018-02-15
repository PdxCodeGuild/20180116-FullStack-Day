// A $( document ).ready() block.
"use strict";

$( document ).ready(function() {
    console.log( "ready!" );
    $('ul.tabs').tabs('select_tab', 'tab_id');
    $('.collapsible').collapsible();
    $(".button-collapse").sideNav();
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
