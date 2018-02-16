
var word = prompt("Type in a word to check and see if it's a palendrome.");

function check_palendrome(a_string)
    if word[:] == word[::-1]:
        alert = ("This is a palendrome.")
    else:
        console.log = ("This is not a palendrome.")




var regularize = function(word) {
    return word.toLowerCase().replace(/[^a-z\d]+/g, '').split('').sort().join('').trim();
}


this.isAnagram = regularize(this.anagram_one) === regularize(this.anagram_two);

var anagram_one = prompt("Type in first entry for anagram check.")
var anagram_two = prompt("Type in second entry for anagram check.")


//function check_anagram(first_string, second_string); {
//    var first_string =  regularize(this.anagram_one)
//    var second_string = regularize(this.anagram_two)
//    if (first_string === second_string) {
//        return.isAnagram = true;




check_anagram(anagram_one, anagram_two);
  if isAnagram {
      alert = ("This is an anagram!")
}

