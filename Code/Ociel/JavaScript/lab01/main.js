
let submit_grade = document.querySelector('#submit_grade');
let output = document.querySelector('#output');

submit_grade.onclick = function () {
    let grade = document.getElementById("grade").value;


    grade = parseInt(grade);
    if (grade >= 90){
        output.innerText = "You get a A!";
    }else if (grade < 90 && grade >= 80){
        output.innerText = "You get a B!";;
    }else if(grade < 80 && grade >= 70){
        output.innerText = "You get a C!";
    }else if (grade < 70){
        output.innerText = "You Failed Son!";
    }else if (!grade){
        output.innerText = "Enter a Value";
    }

};
