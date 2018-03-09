let bq = document.getElementById('bq');
let clicked = document.getElementById('clicked');


function http_get(url, success) {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 1) {
            xhttp.setRequestHeader('Authorization', 'Token token="855df50978dc9afd6bf86579913c9f8b"')
        } else if (this.readyState === 4 && this.status === 200) {
            let data = JSON.parse(xhttp.responseText);
            success(data);
        }
    };
    xhttp.open("GET", url);
    xhttp.send();
}

clicked.addEventListener("click", function() {
    http_get('https://favqs.com/api/quotes/', renderHTML);

});

function renderHTML(data) {
    document.getElementById("bq").innerHTML = data.quotes[0].body + ' - ' + data.quotes[0].author;
}


