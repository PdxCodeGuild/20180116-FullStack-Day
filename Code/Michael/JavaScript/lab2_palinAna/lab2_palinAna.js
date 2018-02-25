// function isPalindrome(str1, str2) {
//     return str1 === str2;
// }
//
// let myStr1 = prompt('enter a word:\n> ');
// let newStr1 = '';
//
// for (let i = myStr1.length - 1; i >= 0; i--) {
//     newStr1 += myStr1[i];
// }
//
//     if (isPalindrome(myStr1, newStr1)){
//         alert(`${myStr1} is a palindrome`);
//     }
//
//     else {
//         alert(`${myStr1} is not a palidrome`);
//     }


function processWord(str1, str2) {
    return str1 === str2;
}

    let str1 = prompt("enter a word:> ");
    let str2 = prompt("enter a word:> ");

    str1 = str1.replace(" ", "");
    str2 = str2.replace(" ", "");

    str1 = str1.split("");
    str2 = str2.split("");

    str1 = str1.sort();
    str2 = str2.sort();

    str1 = str1.join();
    str2 = str2.join();

        if (str1 === str2) {
            alert('are anagrams.');
        }

        else {
            alert('are not anagrams.');
        }