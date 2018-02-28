// globals
let currentInput = 0; //numbers in the input field
let heldNumbers = 0; //numbers being used for stuff
let outputNumbers = ''; //numbers in the outer field
let currentOp = '';
let output = document.querySelector("#output");
let input = document.querySelector(".input");

//jquery init
$(document).ready(function(){
//jquery code goes here
    $(".num").click(function(event) {
        let button_value = event.target.value;
        if (button_value === "backspace") {
          input.value = input.value.slice(0,-1);
        }
      else if (button_value === "clear") {
        input.value = "";
        output.innerText = '';
      }
      else if (button_value === "inverse") {
        input.value = -(input.value);
      }
      else {
      // return button_value
      input.value += button_value;
      }
      currentInput = input.value; //whenever you enter a number this updates
      return input.value;
    });

  $(".op").click(function(event) {
    if ( currentOp === '' ) {
    currentOp = event.target.value;
    let button_value = event.target.value;
    outputNumbers += input.value + currentOp;
    output.innerText = outputNumbers;//updates outertext
    input.value = ''; //clears the current field
    }

    else {
      outputNumbers = eval(outputNumbers + currentInput) ;
      input.value = ''; //clears the current field
      let button_value = event.target.value;

      currentOp = button_value; //update the operand
      outputNumbers += currentOp; //add the operand to the end of variable
      output.innerText = outputNumbers; //display updated outertext
    }
  });
   $("#equals").click(function(event) {
     outputNumbers = eval(outputNumbers + currentInput) ;
     output.innerText = outputNumbers;
     currentOp = '';
     input.value = '';

   });
});
