document.addEventListener("DOMContentLoaded", () => {


const chatForm = document.getElementById("chatForm");

const chatInput = document.getElementById("chatInput");

const chatWindow = document.getElementById("chatWindow");


if(!chatForm) return;


let history = [];



function addMessage(type,message){


    const div=document.createElement("div");


    div.className =
    "chat-msg " + type;


    div.innerHTML = message;


    chatWindow.appendChild(div);


    chatWindow.scrollTop =
    chatWindow.scrollHeight;


}




chatForm.addEventListener("submit", async(e)=>{


e.preventDefault();


const message = chatInput.value.trim();


if(!message) return;



addMessage(
    "user",
    "You: "+message
);



chatInput.value="";



try{


const response = await fetch(
"/api/chatbot/",
{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

message:message,

history:history

})


});



const data = await response.json();


const reply = data.reply || data.error || "I’m not able to respond right now.";

addMessage(
"bot",
"Vidya: "+reply
);



history.push({

role:"user",

content:message

});


history.push({

role:"assistant",

content:data.reply

});



}

catch(error){


addMessage(
"bot",
"Server connection failed"
);


}


});



});