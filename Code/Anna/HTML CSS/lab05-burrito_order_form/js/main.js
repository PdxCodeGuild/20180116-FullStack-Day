// A $( document ).ready() block.
"use strict";

$( document ).ready(function() {
    console.log( "ready!" );
    $('ul.tabs').tabs('select_tab', 'tab_id');
    $('select').material_select();
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


submitForms = function(){
    document.getElementById("form1").submit();
    document.getElementById("form2").submit();
    document.getElementById("form3").submit();
    document.getElementById("form4").submit();
    document.getElementById("form5").submit();
    document.getElementById("form6").submit();
}
