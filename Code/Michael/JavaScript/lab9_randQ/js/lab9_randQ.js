


let bq = document.getElementById('bq');
let clicked = document.getElementById('clicked');


function http_get(url, success) {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState === 1) {
            xhttp.setRequestHeader('Authorization', 'Token token=""')
        } else if (this.readyState === 4 && this.status === 200) {
            let data = JSON.parse(xhttp.responseText);
            success(data);
        }
    };
    xhttp.open("GET", url);
    xhttp.send();
}


function get_data() {

    http_get('https://favqs.com/api/quotes/', function(data) {
        for (let i = 0; i < 10; i++) {
            let node = document.createElement("li");
            node.innerText = data.quotes[i].body + ' - ' + data.quotes[i].author;
            bq.appendChild(node);
        }
    });
}


setInterval(get_data, 10000);


clicked.addEventListener("click", function() {
    get_data();
});



