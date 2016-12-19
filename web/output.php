<?php
$path = 'logs/' . date("Y:m:d") . '.txt';
$file = file_get_contents($path);
$file = str_replace('\n', '<br>', $file);
echo $file;
