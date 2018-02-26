// jquery init

let numbersEntered = 0;
let output = document.querySelector()

$(document).ready(function() {
    // jquery code goes here

    $(".num").click(function(event) {
        let button_value = event.target.value;
        // return button_value;
        let input = document.querySelector(".input");
        if (button_value === "backspace") {
            input.value = input.value.slice(0, -1);
        }

        else if (button_value === "clear") {
            input.value = "";
        }

        else if (button_value === "inverse") {
            input.value = -(input.value);
        }

        else {
            // return button value
            input.value += button_value;
        }
        numbersEntered = input.value;
    });

    $(".op").click(functio(event){
        let button_value = event.target.value;
        numbersEntered += button_value;
        output.innerText += numbersEntered;
        input.value = '';
    });
    $("#equals").click(function(event) {
       output.innerText += numbersEntered;
       input.value = '';

       output.innerText =
    });


    });


    let input = document.querySelector(".input");
    input.value += button_value;

});





//  let button_value = document.querySelector(".num").value;

//document.querySelectorAll(".num").addEventListener("click", function (event) {

//    let button_value = event.target.value;
//    alert(button_value);

//});

