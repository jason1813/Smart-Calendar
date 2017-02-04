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

require "/home/jason/vendor/phpmailer/phpmailer/PHPMailerAutoload.php";

$email="jmmorris2@mail.bradley.edu";
$phone="3097121597@vtext.com";

$mail = new PHPMailer(); // create a new object
$mail->IsSMTP(); // enable SMTP
$mail->SMTPDebug = 1; // debugging: 1 = errors and messages, 2 = messages only
$mail->SMTPAuth = true; // authentication enabled
$mail->SMTPSecure = 'ssl'; // secure transfer enabled REQUIRED for Gmail
$mail->Host = "smtp.gmail.com";
$mail->Port = 465; // or 587
$mail->IsHTML(true);
$mail->Username = "malismartcalendar@gmail.com";
$mail->Password = "iotcalendar";
$mail->SetFrom("example@gmail.com");
$mail->Body = $_POST['message'];

$messageType=$_POST['messageType'];

if ($messageType == "Urgent"){
$mail->AddAddress($phone);
}

else

{
$mail->AddAddress($email);
$mail->Subject = "Calendar Message";
}

 if(!$mail->Send()) {
    echo "Mailer Error: " . $mail->ErrorInfo;
 } else {
    echo "Message has been sent";
 }

?>

<!--
</div>
</body>-->
</html>
