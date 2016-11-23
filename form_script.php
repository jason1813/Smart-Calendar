<?PHP

$from="jmmorris2@mail.bradley.edu";
$email=$_POST['email'];
$subject=$_POST['subject'];
$message=$_POST['message'];

mail($email, $subject, $message);

print "Your message has been sent: </br>$email</br>$subject</br>$message</p>";

?>