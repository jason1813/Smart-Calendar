// idleTimer() takes an optional argument that defines the idle timeout
// timeout is in milliseconds; defaults to 30000
$.idleTimer(4000);

window.location.replace("http://stackoverflow.com");

$(document).bind("idle.idleTimer", function(){
    window.location.replace("http://stackoverflow.com");
 // function you want to fire when the user goes idle
});


$(document).bind("active.idleTimer", function(){
 // function you want to fire when the user becomes active again
});

// pass the string 'destroy' to stop the timer
$.idleTimer('destroy');