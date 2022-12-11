//let play1 = function(){document.getElementById("audio1").play()}
//let play2 = function(){document.getElementById("audio2").play()}
//let play3 = function(){document.getElementById("audio3").play()}
//let play4 = function(){document.getElementById("audio4").play()}
//let play5 = function(){document.getElementById("audio5").play()}
//let play6 = function(){document.getElementById("audio6").play()}
//let play7 = function(){document.getElementById("audio7").play()}
function playsound(x){
    switch(x){
        case 1 : var audio = new Audio('crash.mp3');
                            audio.play();
                            break;
        case 2 : var audio = new Audio('kick-bass.mp3');
                            audio.play();
                            break;
        case 3 : var audio = new Audio('tom-3.mp3');
                            audio.play();
                            break;
        case 4 : var audio = new Audio('tom-1.mp3');
                            audio.play();
                            break;
        case 5 : var audio = new Audio('tom-2.mp3');
                            audio.play();
                            break;
        case 6 : var audio = new Audio('tom-3.mp3');
                            audio.play();
                            break;
        case 7 : var audio = new Audio('tom-4.mp3');
                            audio.play();
                            break;
    }
}