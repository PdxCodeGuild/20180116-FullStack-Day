let container = document.querySelector('#container');
let quoteP = document.querySelector('#quoteP');
let authorP = document.querySelector('#authorP');
let bt_getQuote = document.querySelector('#bt_getQuote');

function success(data) {
    console.log(data);
    $('#container').removeClass('hidden');
    let quote = data.quote.body;
    let author = data.quote.author;
    quoteP.innerText = quote;
    authorP.innerText = "- " + author;
}

function getRandomQuote(url, succeed) {
    console.log("getting a quote");
    bt_getQuote.innerText = "Again!";

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 1) {
        } else if (this.readyState === 4 && this.status === 200) {
            let data = JSON.parse(xhttp.responseText);
            succeed(data);
        } else if (this.readyState === 4 && this.status === 404) {
            quoteP.innerText = "Something's not right...";
        }
    };

    xhttp.open("GET", url);
    xhttp.send();
}

function getFilterQuote() {

    function http_get(url, success) {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 1) {
            xhttp.setRequestHeader('Authorization', 'Token token="<api kep here>"')
        } else if (this.readyState === 4 && this.status === 200) {
            let data = JSON.parse(xhttp.responseText);
            success(data);
        } else if (this.readyState === 4 && this.status === 404) {
            // handle 404
        }
    };
    xhttp.open("GET", url);
    xhttp.send();
    }

}

function make_call(){
    let url = 'https://favqs.com/api/qotd';
    getRandomQuote(url, success);

}

$(document).ready(function() {
    console.log("Ready!");
    $('#bt_getQuote').on('click', make_call);

});
