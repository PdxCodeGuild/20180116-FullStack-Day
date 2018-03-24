$('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year,
    today: 'Today',
    clear: 'Clear',
    close: 'Ok',
    closeOnSelect: false // Close upon selecting a date,
});

// making the bingo part of it work
$('.bingo-box').click(function(){
    $(this).toggleClass('django-green');
    checkWin();
});

// I'm sure there's a better way to do this, but this is about Django, not JavaScript
function checkWin () {
    if ($('#1').hasClass('django-green') && $('#2').hasClass('django-green') && $('#3').hasClass('django-green') && $('#4').hasClass('django-green') && $('#5').hasClass('django-green')) {
        winnerWinner();
    } else if ($('#6').hasClass('django-green') && $('#7').hasClass('django-green') && $('#8').hasClass('django-green') && $('#9').hasClass('django-green') && $('#10').hasClass('django-green')) {
        winnerWinner();
    } else if ($('#11').hasClass('django-green') && $('#12').hasClass('django-green') && $('#14').hasClass('django-green') && $('#15').hasClass('django-green')) {
        winnerWinner();
    } else if ($('#16').hasClass('django-green') && $('#17').hasClass('django-green') && $('#18').hasClass('django-green') && $('#19').hasClass('django-green') && $('#20').hasClass('django-green')) {
        winnerWinner();
    } else if ($('#21').hasClass('django-green') && $('#22').hasClass('django-green') && $('#23').hasClass('django-green') && $('#24').hasClass('django-green') && $('#25').hasClass('django-green')) {
        winnerWinner();
    } else if ($('#1').hasClass('django-green') && $('#6').hasClass('django-green') && $('#11').hasClass('django-green') && $('#16').hasClass('django-green') && $('#21').hasClass('django-green')) {
        winnerWinner();
    } else if ($('#2').hasClass('django-green') && $('#7').hasClass('django-green') && $('#12').hasClass('django-green') && $('#17').hasClass('django-green') && $('#22').hasClass('django-green')) {
        winnerWinner();
    } else if ($('#3').hasClass('django-green') && $('#8').hasClass('django-green') && $('#18').hasClass('django-green') && $('#23').hasClass('django-green')) {
        winnerWinner();
    } else if ($('#4').hasClass('django-green') && $('#9').hasClass('django-green') && $('#14').hasClass('django-green') && $('#19').hasClass('django-green') && $('#24').hasClass('django-green')) {
        winnerWinner();
    } else if ($('#5').hasClass('django-green') && $('#10').hasClass('django-green') && $('#15').hasClass('django-green') && $('#20').hasClass('django-green') && $('#25').hasClass('django-green')) {
        winnerWinner();
    } else if ($('#1').hasClass('django-green') && $('#7').hasClass('django-green') && $('#19').hasClass('django-green') && $('#25').hasClass('django-green')) {
        winnerWinner();
    } else if ($('#21').hasClass('django-green') && $('#17').hasClass('django-green') && $('#9').hasClass('django-green') && $('#5').hasClass('django-green')) {
        winnerWinner();
    } else {
        console.log("No winner yet, but I believe in your ability to error your way through Django!")
    }
}

function winnerWinner() {
    console.log("Chicken dinner");
    window.location.replace("https://stackoverflow.com/search?q=django+error");
}