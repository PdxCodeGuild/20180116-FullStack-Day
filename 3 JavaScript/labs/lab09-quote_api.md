
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


## Version 2

The API also supports browsing quotes by change, and lists 25 per page. Have buttons for changing the page at the bottom. Every time the page is changed, do an HTTP get to `"https://favqs.com/api/quotes?page="+page_id`.

## Version 3 (optional)

Add an `input` field and a `button`, allow users to enter some text and find quotes by using `https://favqs.com/api/quotes/?filter=<text>`. Retrieve the quotes you get in response and show them in a list. Note that if the text has spaces or special characters will have to encode the parameters using [encodeURIComponent](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent) which takes a string and returns a new encoded string.
