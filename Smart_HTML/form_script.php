<html>
<head>
    <title>Mali Messenger</title>
    <link rel="stylesheet" type="text/css" href="./CSS/Smart_Style.css">
</head>

<body>

    <!--tabs at the top-->
    <ul class="toptabs">
        <li><a href="index.html">Calendar</a></li>
        <li><a href="Ads.html">Advertisements</a></li>
        <li id="active"><a>Mali Messenger</a></li>
    </ul>

    <!--all page content. has left margins for the side tabs-->
    <div class="content">

<?PHP

$email="jmmorris2@mail.bradley.edu";
$phone="3097121597@vtext.com";
$subject="Calendar Message";
$message=$_POST['message'];
$messageType=$_POST['messageType'];
$deliveryMethod = $email;

if ($messageType == "Urgent"){ 
    $deliveryMethod = $phone; 
    $subject="";
    }

mail($deliveryMethod, $subject, $message);

print "Professor Mali has received your message!";

?>

</div>
</body>
</html>