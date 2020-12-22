function postToSQL(data){
    let lis = {
        value: data,
        type: "list"
    }
    fetch('/data', {
        method : 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body : JSON.stringify(lis)
    })
    console.log(JSON.stringify( lis ))
}
function addToList(){
	var li = document.createElement("li");
		li.appendChild(document.createTextNode(input.value));
		ul.appendChild(li);
		postToSQL(input.value)
		input.value = "";
}

 function onClickCheckInput(){
	if (input.value !== "") {
		addToList();
	} else {
		alert("Please enter value");
	}	
}

 function onEnterCheckInput(event){
	if (input.value !== "" && event.keyCode === 13) {
		addToList();
	} else if (input.value === "" && event.keyCode === 13) {
		alert("Please enter value");
	}
}

var button = document.getElementById("enter");
var input = document.getElementById("user input");
var ul = document.querySelector("ul");

button.addEventListener("click", onClickCheckInput);
input.addEventListener("keypress", onEnterCheckInput);
