$(document).ready(function() {
    smoothScroll();
    $('.modal').modal();
    $(".dropdown-button").dropdown();
    $('ul.tabs').tabs();
    $(".button-collapse").sideNav();
});
$(function () {
    $(document).scroll(function () {
        let $nav = $("#navbar-custom");
        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    });
});

// sign-in
let $input = $('.form-fieldset > input');

$input.blur(function (e) {
  $(this).toggleClass('filled', !!$(this).val());
});

// navbar
$(window).scroll(function() {
    if ($(".navbar").offset().top > 50) {
        $('#custom-nav').addClass('affix');
        $(".navbar-fixed-top").addClass("top-nav-collapse");
    } else {
        $('#custom-nav').removeClass('affix');
        $(".navbar-fixed-top").removeClass("top-nav-collapse");
    }
});

// Smooth the scroll action
function smoothScroll() {
  $('a[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: target.offset().top
        }, 500);
        return false;
      }
    }
  });
}
