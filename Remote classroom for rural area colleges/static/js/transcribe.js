document.addEventListener("DOMContentLoaded",()=>{


const startBtn =
document.getElementById("startRecording");


const stopBtn =
document.getElementById("stopRecording");


const transcript =
document.getElementById("transcript");


const language =
document.getElementById("language");



if(!startBtn) return;



let recognition;



if(
"webkitSpeechRecognition" in window
){


recognition =
new webkitSpeechRecognition();


recognition.continuous = true;


recognition.interimResults = true;



recognition.onresult = function(event){


let text="";



for(
let i=event.resultIndex;
i<event.results.length;
i++
){


text +=
event.results[i][0].transcript;


}



transcript.value=text;


};



}
else{


alert(
"Speech recognition is not supported in this browser"
);


}




startBtn.onclick = ()=>{


recognition.lang =
language.value;


recognition.start();


};



stopBtn.onclick = ()=>{


recognition.stop();


};



});