let hackContainer = $('#hack-container');

$(document).ready(function(){
    console.log("Ready!");
    let sourceText ='<html>'+(document).all[i=0].innerHTML+'</html>';
    $(document).keydown(
			function (event) {
			    event.preventDefault();
                hackContainer[0].textContent += sourceText.split(/(?=s)/)[i++%100];
			}
		);
});


// popup modal after some seconds
function popUpFirstModal() {
    $('#surprise-modal').modal('show');
}

function popUpSecondModal() {
    $('#surprise-modal-2').modal('show');
}

setTimeout(popUpFirstModal, 10000);
setTimeout(popUpSecondModal, 20000);


