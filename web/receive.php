<?php
$path = 'logs/' . date("Y:m:d") . '.txt';

$get = htmlentities($_POST['data']); //remove the htmlentities function if you want to get accidentally XSS'd
$file = fopen($path, 'w') or die("Something is wrong with your file permissions, please obtain the nessecary rights!");
fwrite($file, $get) or die('error 2');
