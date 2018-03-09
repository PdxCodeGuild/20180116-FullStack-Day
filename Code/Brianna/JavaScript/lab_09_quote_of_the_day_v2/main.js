let api_key = "c4ebc4f09dfaf7a2947a90250196a5a9";  // normally this would be hidden away somewhere. Since we do not care if sample random quotes revokes our access we are posting.
let quote_block = document.getElementById('quote_block'); // Hook into my block quote element

let page_number = document.querySelectorAll('.page_button');

let filter_by = document.querySelector('#filter_by');
let submit_button = document.querySelector('#submit_button');
let key_word = '';

// My first call to Ajax
function http_get(url, success) {   // function to request data from API
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 1) {
            xhttp.setRequestHeader('Authorization', 'Token token="'+ api_key + '"');
            console.log(1)
        } else if (this.readyState === 4 && this.status === 200) {
            let data = JSON.parse(xhttp.responseText);
            console.log(data);
            console.log(2)
            success(data);

        } else if (this.status !== 200) {
            let url = 'https://http.cat/' + this.status;    // add cute cat images for errors
            document.querySelector('#cat_error_img').src = url;  // display cute cat images
            console.log(3)
        }
    };
    xhttp.open("GET", url); // What action we want to take (ie: GET, POST, PUT, or DELETE)
    xhttp.send();
}

console.log(document);

// make button objects
let left_button = document.querySelector('#page_button_1');
let right_button = document.querySelector('#page_button_2');
let current_page = 1;

// get page number value
left_button.onclick = function () {
    if (current_page > 1) {
        curent_page -= 1;
    }
    http_get("https://favqs.com/api/quotes?page="+current_page+"&filter=" + filter_by, function (data) {
        console.log(data);
        quote_block.innerText = data.quote.body + ' ~ ' + data.quote.author;
  });
};

right_button.onclick = function () {
    current_page += 1;
    http_get("https://favqs.com/api/quotes?page="+current_page+"&filter=" + filter_by.value, function (data) {

        console.log(data);
        quote_block.innerText = data.quote.body + ' ~ ' + data.quote.author;
  });
};

// get submit value

submit_button.onclick = function () {
    current_page = 1;
    key_word = filter_by.value;
    console.log("hey")
    http_get("https://favqs.com/api/quotes?page="+current_page+"&filter=" + filter_by.value, function (data) {

        console.log(data);
        quote_block.innerText = data.quote.body + ' ~ ' + data.quote.author;
  });
};




// let url = 'https://favqs.com/api/quotes/?filter=' + search_term.value + '&type=tag&page=' + page_number.value;


// http_get(url, function (data) {
//
//     console.log(data);
//     quote_block.innerText = data.quote.body + ' ~ ' + data.quote.author;
// });

// append multiple quotes to the page
// show and hide “pages” of content when you press a button
// keep track of what quotes are in what page





