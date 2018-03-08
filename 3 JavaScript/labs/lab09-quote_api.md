
# Lab 9: Random Quote


Use the [favqs.com](https://favqs.com/api/) api to show a random quote. To start, use `https://favqs.com/api/qotd` to `GET` a quote, then display it on the page.

```json
{
  "id": 4,
  "author": "Albert Einstein",
  "body": "Make everything as simple as possible, but not simpler.",
  ...
}
```


## Version 2

The API also supports browsing quotes. You can use the `page` and `filter` parameters to get a bunch of quotes. You can add page buttons and/or an `input` field and `button` for filtering.

`"https://favqs.com/api/quotes?page="+page_id+"&filter=" + text`.

Then you can show those quotes in a list.Note that if the text has spaces or special characters will have to encode the parameters using [encodeURIComponent](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent) which takes a string and returns a new encoded string.

In order to get authorization for this request, we need to add a request header with the authorization token using [setRequestHeader](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/setRequestHeader). I'll give you the API key through slack. You can then put it in this altered version of our http_get function, or do it yourself. **Do not commit or push code containing the key to the repo. There are bots that crawl through github looking for keys.**

```javascript
function http_get(url, success) {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 1) {
            xhttp.setRequestHeader('Authorization', 'Token token="<api kep here>"')
        } else if (this.readyState === 4 && this.status === 200) {
            let data = JSON.parse(xhttp.responseText);
            success(data);
        } else if (this.readyState === 4 && this.status === 404) {
            // handle 404
        }
    };
    xhttp.open("GET", url);
    xhttp.send();
}
```