<?php

$files = glob("*.{jpg,gif,png}", GLOB_BRACE);

$str=file_get_contents('../Ads.html');
$oldMessage = explode('<!--images-->', $str);

$beforeFName = '<img class="mySlides" src="./images/';
$afterFName = '" style="width:96%">';

$newMessage = '';

for ($x = 0; $x < count($files); $x++) {
        $newMessage = $newMessage . $beforeFName . $files[$x] . $afterFName;
    }

$str=str_replace($oldMessage[1], $newMessage,$str);
file_put_contents('../Ads.html', $str);

?>