document.querySelector('#redirect').onclick = function() {make_it_so()};

function make_it_so() {
  document.querySelector('#redirect') = location.assign('http://www.google.com'); }