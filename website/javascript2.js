var x = 0;
var t = 1;
var r = 0;

aboutMe();

$(document).ready(function(){
    $(".hi").click(function(){
        $("h3").fadeOut(100);
				$(".hi").fadeOut(100);
				$("h2").fadeOut(1000);
				setTimeout(setStuff, 1000);
        $(".ye").fadeIn(4000);
        $("h1").fadeIn(4000);
        $("input").fadeIn(4000);
        r = 1;
    });

});
function setStuff() {
	var x = "Moody Daas";
	var myText = document.querySelector('h1');
	myText.textContent = x;
  if(t==0){
    document.querySelector("link[href='classy1.css']").href = "classy2.css";
  }
  if(t==1){
    document.querySelector("link[href='psychedelic1.css']").href = "psychedelic2.css";
  }
  if(t==2){
    document.querySelector("link[href='future1.css']").href = "future2.css";
  }
}

function change()
{
  var buttonText = document.querySelector('.ye');
	if(buttonText.textContent == "About Me"){
		$(".ye").fadeOut(1000);
		$("input").fadeOut(1000);
		setTimeout(fI, 1000);
	}
}

function aboutMe()
{
	$("p").fadeOut(0.5);
  $(".ye").fadeOut(0.5);
  $("h1").fadeOut(0.5);
  $("input").fadeOut(0.5);
  $(".div").fadeOut(0.5);
}

function fI(){
	$("p").fadeIn(1000);
}

function theme()
{
  if(x == 0){
    $(".div").fadeIn(0.5);
    x = 1;
    $("h2").fadeOut(0.1);
  }
  else if(x==1){
    if(r==0){
      $(".div").fadeOut(0.5);
      x = 0;
      $("h2").fadeIn(0.1);
    }
    else{
      $(".div").fadeOut(0.5);
      x = 0;
      $("h2").fadeOut(0.1);
    }
  }
}

function makeClassy(){
  if(t!=0){
    if(t==1){
      if(r==0){
         document.querySelector("link[href='psychedelic1.css']").href = "classy1.css";
         t = 0;
       }
       else{
         document.querySelector("link[href='psychedelic2.css']").href = "classy2.css";
         t = 0;
       }
     }
     if(t==2){
       if(r==0){
         document.querySelector("link[href='future1.css']").href = "classy1.css";
         t = 0;
       }
       else{
         document.querySelector("link[href='future2.css']").href = "classy2.css";
         t = 0;
       }
     }
   }
 }
function makePsych(){
  if(t != 1){
     if(t==0){
       if(r==0){
         document.querySelector("link[href='classy1.css']").href = "psychedelic1.css";
         t = 1;
       }
       else{
         document.querySelector("link[href='classy2.css']").href = "psychedelic2.css";
         t = 1;
       }
     }
     if(t==2){
       if(r==0){
         document.querySelector("link[href='future1.css']").href = "psychedelic1.css";
         t = 1;
       }
       else{
         document.querySelector("link[href='future2.css']").href = "psychedelic2.css";
         t = 1;
       }
     }
   }
 }
 function makeFuture(){
   if(t!=2){
     if(t==0){
       if(r==0){
         document.querySelector("link[href='classy1.css']").href = "future1.css";
         t = 2;
       }
       else{
         document.querySelector("link[href='classy2.css']").href = "future2.css";
         t = 2;
       }
     }
     if(t==1){
       if(r==0){
         document.querySelector("link[href='psychedelic1.css']").href = "future1.css";
         t = 2;
       }
       else{
         document.querySelector("link[href='psychedelic2.css']").href = "future2.css";
         t = 2;
       }
     }
   }
 }
