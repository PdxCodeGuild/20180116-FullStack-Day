let x = true; //this part is for the juice later


// operations
function add(number1, number2) {
        return (number1 + number2);
    }
function subtract(number1, number2) {
        return (number1 - number2);
    }
 function multiply(number1, number2) {
        return (number1 * number2);
    }
 function divide(number1, number2) {
        return (number1 / number2);
    }


// calculations
function calculate(number1, number2, operations) {
    let result;
    if (operations === "+") {
        result = add(number1, number2);
    }

    if (operations === "-") {
        result = subtract(number1, number2);
    }

    if (operations === "*") {
        result = multiply(number1, number2);
    }

    if (operations === "/") {
        result = divide(number1, number2);
    }
    return result;
}

// juice
while (x === true){
    if (confirm("welcome to basic calculator! calculate??")) {
        let number1 = parseFloat(prompt("first number?"));
        let operations = prompt("operation? (+, -, *, /");
        let number2 = parseFloat(prompt("second number?"));
        alert(calculate(number1, number2, operations));
    } else {
        x = false;
    }
}
