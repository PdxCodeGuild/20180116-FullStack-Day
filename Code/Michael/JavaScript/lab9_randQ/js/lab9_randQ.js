let bq = document.getElementById('bq');
let clicked = document.getElementById('clicked');

clicked.addEventListener("click", function() {

    let xhttp = new XMLHttpRequest();
    let api_key = '855df50978dc9afd6bf86579913c9f8b';

    xhttp.open('GET', 'https://favqs.com/api/quotes/');

    xhttp.onreadystatechange = function() {
        xhttp.setRequestHeader('Authorization', 'Token token="' + api_key + '"');
    };

    xhttp.onload = function() {
        let ourData = JSON.parse(xhttp.responseText);
        renderHTML(ourData)
    };
    xhttp.open("GET", url);
    xhttp.send();

});

function renderHTML(data) {
    let htmlString = "";
    bq.insertAdjacentHTML("beforeend", htmlString);

}
