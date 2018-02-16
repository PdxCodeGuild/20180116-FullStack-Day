
var word = prompt("Type in a word to check and see if it's a palindrome.");

function check_palendrome(a_string)
{
    if (a_string === a_string.reverse()) {
        alert("This is a palendrome.");
    }
    else {
        alert("This is not a palendrome.");
    }
};

check_palendrome(word);


var regularize = function(word) {
    return word.toLowerCase().replace(/[^a-z\d]+/g, '').split('').sort().join('').trim();
};




var anagram_one = prompt("Type in first entry for anagram check.");
var anagram_two = prompt("Type in second entry for anagram check.");

var isAnagram = regularize(anagram_one) === regularize(anagram_two);
//function check_anagram(first_string, second_string); {
//    var first_string =  regularize(this.anagram_one)
//    var second_string = regularize(this.anagram_two)
//    if (first_string === second_string) {
//        return.isAnagram = true;






if (isAnagram) {
    alert("This is an anagram!");
};


