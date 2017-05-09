var slideIndex = 0;

window.setInterval(carousel, 20000); // Change image every 20 seconds

function carousel()
{
    var i;
    var x = document.getElementsByClassName("mySlides");
    for (i = 0; i < x.length; i++)
    {
        x[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex >= x.length)
    {
        slideIndex = 0;
    }
    x[slideIndex].style.display = "block";
}

