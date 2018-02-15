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

// Function for sending all of the forms
window.addEventListener("load", function () {
  function sendData() {
    var XHR = new XMLHttpRequest();

    // Bind the FormData object and the form element
    var FD = new FormData(form);

    // Define what happens on successful data submission
    XHR.addEventListener("load", function(event) {
      alert(event.target.responseText);
    });

    // Define what happens in case of error
    XHR.addEventListener("error", function(event) {
      alert('Oups! Something goes wrong.');
    });

    // Set up our request
    XHR.open("POST", "https://requestb.in/1f84cwu1");

    // The data sent is what the user provided in the form
    XHR.send(FD);
  }

  // Access the form element...
  var form1 = document.getElementById("form1");
  var form2 = document.getElementById("form2");
  var form3 = document.getElementById("form3");
  var form4 = document.getElementById("form4");

  // ...and take over its submit event.
  form1.addEventListener("submit", function (event) {
    event.preventDefault();

    sendData();
  });
  form2.addEventListener("submit", function (event) {
    event.preventDefault();

    sendData();
  });
  form3.addEventListener("submit", function (event) {
    event.preventDefault();

    sendData();
  });
  form4.addEventListener("submit", function (event) {
    event.preventDefault();

    sendData();
  });
});


//
//
// submitForms = function(){
//
//
//     let formObj = {
//
//
//     }
//
//     myobj['name']
//     myobj.name
//
//     // get each input field, get the value using .val()
//     // put all that into one giant javascript object
//     // use ajax to submit the data
//
//
//
//
//     // for (let i=1; i<7; ++i) {
//     //     let form = $('#form'+i);
//     //     form.attr('action', 'https://requestb.in/1f84cwu1');
//     //     form.attr('method', 'post');
//     //     form[0].submit();
//     // }
//
//
//         $.ajax({
//         type: "POST",
//         url: "https://requestb.in/1f84cwu1",
//         data: formObj
//     });
// }
//
