// window.onload = function () {

    // Get the word we are either encrypting or decrypting
    let input_phrase = document.getElementById("code_input");

    // Figure out if we are encypting or decrypting the word
    let translate = document.getElementById("encryption_type");

    // Find out by how much the user would like to rotate the code.
    let rotation = document.getElementById("rotation");

    //Get the various elements from submission... needed??
    let encrypt = document.getElementById("submit_code");

    //Print results to the display
    let output_div = document.querySelector(".code_output");

    console.log(input_phrase, translate, rotation, encrypt);

    function encode2(string, rotation, encryption_type) {
        let result = "", code;
        if (encryption_type === "Decrypt") {
            rotation = -(rotation);
        }
        for (let i = 0; i < string.length; ++i) {
            if (string.charCodeAt(i) > 65 && string.charCodeAt(i) <= 90) {
                code = string.charCodeAt(i) - 65;
                code += rotation % 26;
                code += 65;
            }
            else if (string.charCodeAt(i) >= 97 && string.charCodeAt(i) <= 122) {
                code = string.charCodeAt(i) - 97;
                code += rotation % 26;
                code += 97;
            }
            else if (string.charCodeAt(i) < 65) {
                code = string.charCodeAt(i);
            }
            result += String.fromCharCode(code);
        }

        //document.getElementById('output_div').innerHTML = "<div><p>" + result + "</p></div>"
        pElement = document.createElement("p");
        divElement = document.createElement("div");
        divElement.appendChild(pElement);
        pElement.append(result);
        // make p into child of div, append result to p. /set value



    }


    encrypt.addEventListener("click", encode2(input_phrase, rotation, translate));


   // encrypt.onclick = function () {
    //    encode2(input_phrase, rotation, translate);
//}
// }


