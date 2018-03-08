let code_element = document.querySelector('#code_element');

// let column_limit = 79;

function http_get(url, success) {  // making AJAX function
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {  // Once the page has loaded
        if (this.readyState === 4 && this.status === 200) { // Making sure that the page is ready and there are no initial errors
            success(xhttp.responseText);
        }
    };
    xhttp.open("GET", url);
    xhttp.send();
}

let url = 'https://raw.githubusercontent.com/PdxCodeGuild/20180116-FullStack-Day/master/Code/Brianna/Python/lab_26_scroller_adventure_game/platform_scroller.py';
let code = '';
let shown_chars = 0;

http_get(url, function(data) {
  code = data;
  shown_chars = 0;
});


document.body.onkeypress = function() {
  shown_chars += 4;
  if (shown_chars >= code.length) {
    shown_chars = 0;
  }
  code_element.innerText = code.substring(0, shown_chars);
  hljs.highlightBlock(code_element);
  window.scrollTo(0,document.body.scrollHeight);
};
