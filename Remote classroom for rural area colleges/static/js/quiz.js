document.addEventListener("DOMContentLoaded",()=>{


const button =
document.getElementById("generateQuiz");


if(!button) return;



button.addEventListener("click",async()=>{


const topic =
document.getElementById("quizTopic").value;


const difficulty =
document.getElementById("quizDifficulty").value;


const count =
document.getElementById("quizCount").value;



const result =
document.getElementById("quizResult");



if(!topic){

result.innerHTML =
"Enter a topic";

return;

}




try{


const response =
await fetch(
"/api/quiz/",
{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

topic:topic,

difficulty:difficulty,

count:count

})

}

);



const data =
await response.json();


const quizText = data.quiz || data.error || "Unable to generate quiz";

result.innerHTML =
quizText;



}

catch(error){


result.innerHTML =
"Unable to generate quiz";


}



});



});