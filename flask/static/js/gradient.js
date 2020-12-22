function postTSQL(color_left, color_right){
    let lis = {
        color_left: color_left,
        color_right: color_right,
        type: "colors"
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


function setBackground(){
	body.style.background = "linear-gradient(to right, " + color1.value + ", " + color2.value+" )";
	css.textContent = body.style.background + ";";
	postTSQL(color1["value"], color2["value"]);
}

var css = document.querySelector("h3");
var color1 = document.querySelector(".color1");
var color2 = document.querySelector(".color2");
var body = document.getElementById("gradient");

color1.addEventListener("input", setBackground);
color2.addEventListener("input", setBackground);