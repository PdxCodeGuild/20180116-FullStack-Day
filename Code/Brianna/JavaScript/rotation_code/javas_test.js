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
    let output = document.getElementbyID("code_output");

    encrypt.onclick = function(){
        encode2(input_phrase, rotation);

    };

    function rotation_function(string, rotation, encryption_type) {
        let output_text = '';

        for (let i = 0; i < string.length; ++i) {
            let character = string[i].toUpperCase();
            let index = [A - Z].index(character);
            index += rotation;
            if (encryption_type === decrypt) {
                rotation = -(rotation);
                output_text += output_text.append([A - Z][i]);
            } else {
                output_text += output_text.append([A - Z][i]);
            }
        }
        return output_text;
    }

    alert(rotation_function(input_phrase, rotation, translate))
};


// use unicode value of letter

function encode(str, rotation){
    let array = [];

    for (i=0; i<= str.length; ++i) {
        if (rotation <= 13) {
            if (str.charCodeAt(i) > 65 && str.charCodeAt(i) < 77) {
                array.push(String.fromCharCode(str.charCodeAt(i) + rotation));
            }
            else if (str.charCodeAt(i) >= 78 && str.charCodeAt(i) <= 90) {
                array.push(String.fromCharCode(str.charCodeAt(i) - rotation));
            }
            else if (str.charCodeAt(i) < 65) {
                array.push(str[i]);
            }
        }
        else if (rotation > 13) {

        }
    }
    document.write(array.join.(""));
}

encode();

function encode2 (string, rotation) {
    let result = "", code;
    for (let i=0; i<string.length; ++i) {
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
    alert(result);
}

encode2();