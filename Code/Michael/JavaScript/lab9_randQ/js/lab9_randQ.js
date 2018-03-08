let bq = document.getElementById('bq');
let clicked = document.getElementById('clicked');

clicked.addEventListener("click", function() {

    let ourRequest = new XMLHttpRequest();
    let api_key = '855df50978dc9afd6bf86579913c9f8b';

    ourRequest.open('GET', 'https://favqs.com/api/quotes/');

    ourRequest.onreadystatechange = function() {
        ourRequest.setRequestHeader('Authorization', 'Token token="' + api_key + '"');
    };

    ourRequest.onload = function() {
        let ourData = JSON.parse(ourRequest.responseText);
        renderHTML(ourData)
    };

});

function renderHTML(data) {
    let htmlString = "";
    bq.insertAdjacentHTML("beforeend", htmlString);

}


