let randomURLs = ['http://www.nytimes.com/interactive/magazine/you-made-it.html', 'http://geektyper.com/fsociety/', 'https://www.fastcodesign.com/3048941/why-googles-deep-dream-ai-hallucinates-in-dog-faces', 'https://www.buzzfeed.com/charliewarzel/the-terrifying-future-of-fake-news', 'https://bl.ocks.org/mbostock/9539958'];
let pickedURL = '';

// pick a random URL
function pick() {
    pickedURL = randomURLs[Math.floor(Math.random() * randomURLs.length)];
}

function redirect() {
    pick();
    location.assign(pickedURL);
}

// Load when ready.
$( document ).ready(function() {
    console.log( "ready!" );
    // wait 5 seconds
    setTimeout(redirect, 4400);
    // redirect
});
