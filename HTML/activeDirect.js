var IDLE_TIMEOUT = 10; //seconds
var _idleSecondsCounter = 0;

document.onclick = function() 
{
    _idleSecondsCounter = 0;
}

document.onmousemove = function()
{
    _idleSecondsCounter = 0;
}

document.onkeypress = function() 
{
    _idleSecondsCounter = 0;
}

function getText()
{
    var textrequest = new XMLHttpRequest();
    textrequest.open("GET", "temporary/message.txt", false);
    textrequest.send(null);
    //window.alert(textrequest.status);
    
    if (textrequest.readyState === 4 && textrequest.status === 200) 
    {
        var type = textrequest.getResponseHeader("Content-Type");
        if (type.indexOf("text") !== 1) 
        {
           var textfile = " ";
           textfile = textrequest.responseText;
           
           if(textfile.includes("b")) window.location.href = "index.html";
           //else window.alert(textfile);
        }
    }
}

function CheckIdleTime() 
{
    if (_idleSecondsCounter < IDLE_TIMEOUT)
    {
        _idleSecondsCounter++;
    } else {
        getText();
    }
}

function startTimeout()
{
    window.setInterval(CheckIdleTime, 1000);
}
