let api_key = "c4ebc4f09dfaf7a2947a90250196a5a9";  // normally this would be hidden away somewhere. Since we do not care if sample random quotes revokes our access we are posting.
let quote_div = document.getElementById('quote_div'); // hook into my div that contains the quote
let quote_block = document.getElementById('quote_block'); // Hook into my block quote element
let key_word = document.getElementById('key_word');
let page_button_1 = document.getElementById('page_button_1');
let page_button_2 = document.getElementById('page_button_2');
let page_button_3 = document.getElementById('page_button_3');
let page_button_4 = document.getElementById('page_button_4');
let page_button_5 = document.getElementById('page_button_5');


let url = 'https://favqs.com/api/quotes?page=1';


function http_get(url, success) {   // function to request data from API
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 1) {
            xhttp.setRequestHeader('Authorization', 'Token token="'+ api_key + '"');
        } else if (this.readyState === 4 && this.status === 200) {
            let data = JSON.parse(xhttp.responseText);
            console.log(data);
            success(data);
        } else if (this.status !== 200) {
            let url = 'https://http.cat/' + this.status;    // add cute cat images for errors
            document.querySelector('#cat_error_img').src = url;  // display cute cate images
        }
    };
    xhttp.open("GET", url); // What action we want to take (ie: GET, POST, PUT, or DELETE)
    xhttp.send();
}




// let url = 'https://favqs.com/api/quotes/?filter=' + search_term.value + '&type=tag&page=' + page_number.value;

function getQuotes(page_number) {
    if (page_number === 2 || page_number === 3 || page_number === 4 || page_number === 5) {
        if (key_word.value != null) {
            let url = 'https://favqs.com/api/quotes/?filter=' + key_word.value + '&type=tag&page=' + page_number;
        } else {
            let url = 'https://favqs.com/api/quotes?page=' + page_number;
        }
    }
    http_get(url, function (data) {

        let total_pages = 5;
        quote_div.innerHTML = '';
        quote_block.innerText = '';
        let quotes = data.quotes;
        for (let i=0; i < quotes.length; ++i) {
            let quote = quotes[i].body;
            let author = quotes[i].author;
            let quote_block = document.createElement('div');
            quote_block.innerHTML ='<blockquote>' + '"' + quote + '"' + '~' + author + '</blockquote>';
            quote_div.appendChild(quote_block);
        }
    });
}

page_button_1.onclick = function () {
    getQuotes(1);
    window.scrollTo(0,0);
};
page_button_2.onclick = function () {
    getQuotes(2);
    window.scrollTo(0,0);
};
page_button_3.onclick = function () {
    getQuotes(3);
    window.scrollTo(0,0);
};
page_button_4.onclick = function () {
    getQuotes(4);
    window.scrollTo(0,0);
};
page_button_5.onclick = function () {
    getQuotes(5);
    window.scrollTo(0,0);
};




