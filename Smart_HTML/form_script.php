<?PHP

$email="jmmorris2@mail.bradley.edu";
$subject="Calendar Message";
$message=$_POST['message'];

mail($email, $subject, $message);

print "Your message has been sent: </br>$email</br>$subject</br>$message</p>";

?>