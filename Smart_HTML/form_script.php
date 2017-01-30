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

// $email="jmmorris2@mail.bradley.edu";
// $phone="3097121597@vtext.com";
// $subject="Calendar Message";
// $message=$_POST['message'];
// $messageType=$_POST['messageType'];
// $deliveryMethod = $email;

// if ($messageType == "Urgent"){ 
//     $deliveryMethod = $phone; 
//     $subject="";
//     }

// mail($deliveryMethod, $subject, $message);

// print "Professor Mali has received your message!";

$mail = new PHPMailer(true);
$email="jmmorris2@mail.bradley.edu";
$name = Jason;
$email_from = gmail.com;
$name_from = jason;

if($send_using_gmail){
    $mail->IsSMTP(); // telling the class to use SMTP
    $mail->SMTPAuth = true; // enable SMTP authentication
    $mail->SMTPSecure = "ssl"; // sets the prefix to the servier
    $mail->Host = "smtp.gmail.com"; // sets GMAIL as the SMTP server
    $mail->Port = 465; // set the SMTP port for the GMAIL server
    $mail->Username = "slinkymation@gmail.com"; // GMAIL username
    $mail->Password = "2fartpoo2"; // GMAIL password
}

$mail->AddAddress($email, $name);
$mail->SetFrom($email_from, $name_from);
$mail->Subject = "My Subject";
$mail->Body = "Mail contents";

try{
    $mail->Send();
    echo "Success!";
} catch(Exception $e){
    //Something went bad
    echo "Fail - " . $mail->ErrorInfo;
}

?>

</div>
</body>
</html>