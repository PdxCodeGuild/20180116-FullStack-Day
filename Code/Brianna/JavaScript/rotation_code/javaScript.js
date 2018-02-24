window.onload = function () {

    // Get the word we are either encrypting or decrypting
    let input_phrase = document.getElementbyID("code_input");

    // Figure out if we are encypting or decrypting the word
    let translate = document.getElementbyID("encryption_type");

    // Find out by how much the user would like to rotate the code.
    let rotation = document.getElementbyID("rotation");

    //Get the various elements from submission... needed??
    let encrypt = document.getElementbyID("submit_code");

    //Print results to the display
    let output_div = document.querySelector(".code_output");


    function encode2(string, rotation, encryption_type) {
        let output
    .
        innerHTML = "", code;
        if (encryption_type === decrypt) {
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
        return output;
    }


    encrypt.onclick = function () {
        encode2(input_phrase, rotation, translate);

    }
}


