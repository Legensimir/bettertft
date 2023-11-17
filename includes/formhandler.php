<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $nameinput = htmlspecialchars($_POST["nameInput"]);

    echo "data:";
    echo "<br>";
    echo $nameinput;

}