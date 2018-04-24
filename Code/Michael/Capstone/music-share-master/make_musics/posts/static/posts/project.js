


const app = document.getElementById('root');

const contained = document.createElement('div');
contained.setAttribute('class', 'container');

app.appendChild(contained);



function http_get(url, success) {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            let data = JSON.parse(xhttp.responseText);
            success(data);
        }
    };
    xhttp.open("GET", url);
    xhttp.send();
}



http_get('https://api.discogs.com/artists/5/releases?sort=year&sort_order=desc', function(data) {
    for (let i=0; i<data.releases.length; ++i) {
        console.log(data.releases[i].title);
    }
});


//let request = new XMLHttpRequest();

// request.open('GET', 'https://ghibliapi.herokuapp.com/films', true);
//request.open('GET', 'https://api.discogs.com/releases', true);
// request.open('GET', 'https://api.discogs.com/artists/5/releases?sort=year&sort_order=desc', true);
//
// request.onload = function () {
//     let data = JSON.parse(this.response);
//
//     if (request.status >= 200 && request.status < 400) {
//         data.forEach(movie => {
//
//             const card = document.createElement('div');
//             card.setAttribute('class', 'card');
//
//             const h5 = document.createElement('h5');
//             h5.textContent = movie.title;
//
//             const p = document.createElement('p');
//             movie.description = movie.description.substring(0, 300);
//             p.textContent = `${movie.description}...`;
//
//             contained.appendChild(card);
//             card.appendChild(h5);
//             card.appendChild(p);
//         });
//     } else {
//
//         const errorMessage = document.createElement('margee');
//         errorMessage.textContent = `Nope`;
//         app.appendChild(errorMessage);
//
//     }
// }
//
// request.send();
