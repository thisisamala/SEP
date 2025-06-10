function handler() {
    alert("hello");
}
function tester() {
    alert("hello");
}

const btn = document.getElementById("btn");
let user = "John";
btn.addEventListener("click",function(e){alert("HI "+ user +"Button clicked");});