let bq = document.getElementById('bq');
let clicked = document.getElementById('clicked');


function http_get(url, success) {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 1) {
            xhttp.setRequestHeader('Authorization', 'Token token=""')
        } else if (this.readyState === 4 && this.status === 200) {
            let data = JSON.parse(xhttp.responseText);
            success(data);
        }
    };
    xhttp.open("GET", url);
    xhttp.send();

    window.onload = function() {
    function http_get() {
    }
    setInterval(http_get, 5000);

};


clicked.addEventListener("click", function() {
    http_get('https://favqs.com/api/quotes/', renderHTML);

});

function renderHTML(data) {
    document.getElementById("bq").innerHTML = data.quotes[0].body + ' - ' + data.quotes[0].author;


}}


