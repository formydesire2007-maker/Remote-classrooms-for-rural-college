document.addEventListener("DOMContentLoaded",()=>{


const button =
document.getElementById("translateBtn");


if(!button) return;



button.addEventListener("click",async()=>{


const text =
document.getElementById("translateText").value;


const direction =
document.getElementById("direction").value;



const output =
document.getElementById("translationResult");



if(!text){

output.innerHTML =
"Enter text";

return;

}




try{


const response =
await fetch(
"/api/translate/",
{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

text:text,

direction:direction

})


});



const data =
await response.json();


const translation = data.translation || data.error || "Translation failed";

output.innerHTML =
translation;



}

catch(error){


output.innerHTML =
"Translation failed";


}



});



});