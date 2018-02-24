
let submit_grade = document.querySelector('#submit_grade');

submit_grade.onclick = function () {
    let grade = document.getElementById("grade").value;

    grade = parseInt(grade);
    if (grade >= 90){
        alert("You get an A");
    }else if (grade < 90 && grade >= 80){
        alert("You get a B");
    }else if(grade < 80 && grade >= 70){
        alert("You get a C");
    }else if (grade < 70){
        alert("You failed Son");
    }else if (!grade){
        alert("Please enter a integer value");
    }
}
