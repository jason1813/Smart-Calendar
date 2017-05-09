var myIndex = 0;

function carousel()
{
    var i;
    var x = document.getElementsByClassName("mySlides");
    for (i = 0; i < x.length; i++)
    {
        x[i].style.display = "none";
    }
    myIndex++;
    if (myIndex >= x.length)
    {
        myIndex = 0;
    }
    x[myIndex].style.display = "block";
    setTimeout(carousel, 15000); // Change image every 15 seconds
}

carousel();
