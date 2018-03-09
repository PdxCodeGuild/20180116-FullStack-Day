let api_key = "c4ebc4f09dfaf7a2947a90250196a5a9";  // normally this would be hidden away somewhere. Since we do not care if sample random quotes revokes our access we are posting.
let quote_block = document.getElementById('quote_block'); // Hook into my block quote element
let page_number = document.querySelector('#page_button');
let filter_by = document.querySelector('#filter_by');


// My first call to Ajax
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

console.log(document);

// Build a function to get quotes and append them to the page.
function get_quotes(key_word) {
  let url = "https://favqs.com/api/quotes?page="+page_number+"&filter=" + text;
  http_get(url, function(data) {

    filter_by.innerHTML = '';
    quote_block.innerHTML = '';

    let total_pages = data.total_pages;
    for (let i=0; i<total_pages; ++i) {
      let page_button = document.createElement('button');
      page_bt.innerText = (i+1);
      page_bt.onclick = function() {
        get_users(i+1);
      };
      filter_by.appendChild(page_button);
    }
    let quote = data.quote.body;
    for (let i=0; i<quote.length; ++i) {

      quote_block.innerText = data.quote.body + ' ~ ' + data.quote.author

      let img = document.createElement('img');
      img.src = img_url;

      let user_div = document.createElement('div');
      user_div.appendChild(quote);

      users_div.appendChild(user_div);

    }
  });

//
if (page_number === 2 || page_number === 3 || page_number === 4 || page_number === 5) {
    let url = 'https://favqs.com/api/quotes/?filter=&type=tag&page=' + page_number.value;
} else {
    let url = 'https://favqs.com/api/quotes/?filter=&type=tag&page=1'
}


// let url = 'https://favqs.com/api/quotes/?filter=' + search_term.value + '&type=tag&page=' + page_number.value;

http_get(url, function (data) {

    console.log(data);
    quote_block.innerText = data.quote.body + ' ~ ' + data.quote.author;
});





