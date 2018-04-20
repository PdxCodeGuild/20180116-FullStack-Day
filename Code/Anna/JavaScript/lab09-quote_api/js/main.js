let container = document.querySelector('#container');
let quoteP = document.querySelector('#quoteP');
let authorP = document.querySelector('#authorP');
let bt_getQuote = document.querySelector('#bt_getQuote');
let keywordInput = document.querySelector('#keyword');
let bt_getQuotes = document.querySelector('#bt_getQuotes');

function displayQuote(data) {
    console.log(data);
    $('#container').removeClass('hidden');
    let quote = data.quote.body;
    let author = data.quote.author;
    quoteP.innerText = quote;
    authorP.innerText = "- " + author;
}

function displayMultiple(data) {
    console.log(data);
    $('#container').removeClass('hidden');
    let quote = data.quotes[0].body;
    let author = data.quotes[0].author;
    let current_quote = 0;
    quoteP.innerText = quote;
    authorP.innerText = "- " + author;
    $('#bt_getQuote').addClass('hidden');
    $('#bt_getQuotes').addClass('hidden');
    $('#bt_next').removeClass('hidden');
    $('#bt_next').on('click', function(){
        current_quote += 1;
        if (current_quote < data.quotes.length) {
            let quote = data.quotes[current_quote].body;
            let author = data.quotes[current_quote].author;
            quoteP.innerText = quote;
            authorP.innerText = "- " + author;
        } else {
            $('#bt_getQuote').removeClass('hidden');
            $('#bt_another').addClass('hidden');
            quoteP.innerText = "No more quotes, search a keyword or press 'Inspire Me' to get a random quote.";
            authorP.innerText = " ";
        }
    });
}

function displayFiltered(data) {
    console.log(data);
    $('#container').removeClass('hidden');
    let quote = data.quotes[0].body;
    let author = data.quotes[0].author;
    let current_quote = 0;
    quoteP.innerText = quote;
    authorP.innerText = "- " + author;
    $('#bt_getQuote').addClass('hidden');
    $('#bt_getQuotes').addClass('hidden');
    $('#bt_another').removeClass('hidden');
    $('#bt_another').on('click', function(){
        current_quote += 1;
        if (current_quote < data.quotes.length) {
            let quote = data.quotes[current_quote].body;
            let author = data.quotes[current_quote].author;
            quoteP.innerText = quote;
            authorP.innerText = "- " + author;
        } else {
            $('#bt_getQuote').removeClass('hidden');
            $('#bt_another').addClass('hidden');
            quoteP.innerText = "No more quotes, search another keyword or press 'Inspire Me' to get a random quote.";
            authorP.innerText = " ";
        }
    });

}

function getRandomQuote(url, success) {
    console.log("getting a quote");
    bt_getQuote.innerText = "Again!";

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 1) {
        } else if (this.readyState === 4 && this.status === 200) {
            let data = JSON.parse(xhttp.responseText);
            success(data);
        } else if (this.readyState === 4 && this.status === 404) {
            quoteP.innerText = "Something's not right...";
        }
    };

    xhttp.open("GET", url);
    xhttp.send();
}

function getFilterQuote(url, success) {
    console.log(keywordInput.value);

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 1) {
            xhttp.setRequestHeader('Authorization', 'Token token="<sorry git robots, no token for you!>"');  // won't work without api token!
        } else if (this.readyState === 4 && this.status === 200) {
            let data = JSON.parse(xhttp.responseText);
            success(data);
        } else if (this.readyState === 4 && this.status === 404) {
            quoteP.innerText = "Something's not right...";
        }
    };
    xhttp.open("GET", url);
    xhttp.send();

}

function getMultipleQuote(url, success) {
    console.log("getting 25 quotes");

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 1) {
            xhttp.setRequestHeader('Authorization', 'Token token="<sorry git robots, no token for you!>"');  // won't work without api token!
        } else if (this.readyState === 4 && this.status === 200) {
            let data = JSON.parse(xhttp.responseText);
            success(data);
        } else if (this.readyState === 4 && this.status === 404) {
            quoteP.innerText = "Something's not right...";
        }
    };

    xhttp.open("GET", url);
    xhttp.send();
}

function makeCall(){
    let url = 'https://favqs.com/api/qotd';
    getRandomQuote(url, displayQuote);
}

function makeNewCall() {
    let url = 'https://favqs.com/api/quotes/?filter=' + keywordInput.value;
    getFilterQuote(url, displayFiltered);
}

function makeMultipleCall() {
    let url = 'https://favqs.com/api/quotes/';
    getMultipleQuote(url, displayMultiple);
}

$(document).ready(function() {
    console.log("Ready!");
    $('#bt_getQuote').on('click', makeCall);
    $('#bt_keyword').on('click', makeNewCall);
    $('#bt_getQuotes').on('click', makeMultipleCall);
});
