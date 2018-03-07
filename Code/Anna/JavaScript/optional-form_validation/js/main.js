$(document).ready(function() {
    console.log("Ready!");
    $('#bt_getQuote').on('click', makeCall);
    $('#bt_keyword').on('click', makeNewCall);
});
