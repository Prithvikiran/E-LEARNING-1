
var session_seconds = "00";
var session_minutes = 25;


var click_sound = new Audio("/static/sounds/click.mpeg");
var bell = new Audio("feynman/static/sounds/bell.mpeg");


function template() {
  document.getElementById("minutes").innerHTML = session_minutes;
  document.getElementById("seconds").innerHTML = session_seconds;
}

function start_timer() {
  click_sound.play();


  session_minutes = 24;
  session_seconds = 59;

  
  document.getElementById("minutes").innerHTML = session_minutes;
  document.getElementById("seconds").innerHTML = session_seconds;

  var minutes_interval = setInterval(minutesTimer, 60000);
  var seconds_interval = setInterval(secondsTimer, 1000);


  function minutesTimer() {
    session_minutes = session_minutes - 1;
    document.getElementById("minutes").innerHTML = session_minutes;
  }


  function secondsTimer() {
    session_seconds = session_seconds - 1;
    document.getElementById("seconds").innerHTML = session_seconds;


    if (session_seconds <= 0) {
      if (session_minutes <= 0) {
        
        clearInterval(minutes_interval);
        clearInterval(seconds_interval);

        document.getElementById("done").innerHTML =
          "Session Completed!! Take a Break";

     
        document.getElementById("done").classList.add("show_message");


        bell.play();
      }

      session_seconds = 60;
    }
  }
}