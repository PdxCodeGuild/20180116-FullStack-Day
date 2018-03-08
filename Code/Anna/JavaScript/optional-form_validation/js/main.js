$(document).ready(function() {
    console.log("Ready!");
    $('#bt_submit').on('click', submitForm);
});


function validateSSN() {
   let pattern = new RegExp("\d{3}[\-]\d{2}[\-]\d{4}");
   let ssn = document.querySelector("#ssn");
   let res = pattern.test(ssn.value);
   if(!res){
    x.value = x.value
        .match(/\d*/g).join('')
        .match(/(\d{0,3})(\d{0,2})(\d{0,4})/).slice(1).join('-')
        .replace(/-*$/g, '');
   }
}

function submitForm() {
    console.log("submitted");
    $('#headDiv').addClass('hidden');
    $('#resultDiv').removeClass('hidden');
}
