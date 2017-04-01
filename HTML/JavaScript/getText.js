getText();

function getText()
{
    var textrequest = new XMLHttpRequest();
    textrequest.open('GET', "../message.txt", false);
    textrequest.send(null);
    
    if (textrequest.readyState === 4 && textrequest.status === 200) 
    {
        var type = textrequest.getResponseHeader('Content-Type');
        if (type.indexOf("text") !== 1) 
        {
           var textfile = ' ';
           textfile = textrequest.responseText;
           
           if(textfile.includes("b")) window.location.href = "http://localhost:8000/Calendar.html";
           //else window.alert(textfile);
        }
    }
    setTimeout(getText, 4000);
}
