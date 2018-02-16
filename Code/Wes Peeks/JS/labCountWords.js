
function countWords() {
    var words = document.getElementById("watergate").innerText;
    words = words.replace(/(^\s*)|(\s*$)/gi,"");
    words = words.replace(/\n /,"\n");
    words = words.split(' ').length;
    document.getElementById("wordcount").innerText = words;
}