let container = document.querySelector('#container');
let quoteP = document.querySelector('#quoteP');
let authorP = document.querySelector('#authorP');



function success(data) {
    console.log(data);
    $('#container').toggleClass('hidden');
    let quote = data.quote.body;
    let author = data.quote.author;
    quoteP.innerText = quote;
    authorP.innerText += author;
}

function getQuote(url, succeed) {
    console.log("getting a quote");

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 1) {
            // xhttp.setRequestHeader('Authorization', 'Token token="<api kep here>"')
        } else if (this.readyState === 4 && this.status === 200) {
            let data = JSON.parse(xhttp.responseText);
            succeed(data);
        } else if (this.readyState === 4 && this.status === 404) {
            // handle 404
        }
    };

    xhttp.open("GET", url);    // original: ("GET", url)
    xhttp.send();
}

function make_call(){
    let url = 'https://favqs.com/api/qotd';
    getQuote(url, success);

}

$(document).ready(function() {
    console.log("Ready!");
    $('#bt_getQuote').on('click', make_call);

});
