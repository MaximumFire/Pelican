<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="/css/Darkmode/signin.css">
    <link rel="shortcut icon" href="images/favicon.ico" />
    <title>Pelican</title>
</head>
<body>

<script>
        window.onload = event => {
            document.getElementById("username-display").innerHTML = localStorage.getItem("NAME");
        };
    </script>

    <div class="header typewriter">
        <img src="images/logo.svg">
        <h1>Pelican: Security where it counts</h1>   
    </div>

    <div class="topnav">
        <a href="home.php">Home</a>
        <a href="download.php">Download</a>
        <a href="support.php">Support</a>
        <a href="about.php">About</a>
        <a href="login.php">Login</a>
        <a href="register.php">Register</a>
        <a href="tos.php">ToS</a>

        <p id="username-display" class="pos-right"></p>
    </div>

    <div class="login-page">
        <div class="form">
            <form class="login-form" action="" method="post">
            <input name="email" type="text" placeholder="email" value=""/>
            <input name="pass" type="password" placeholder="password" value=""/>
            <button name="button" onclick="setName()">Sign In</button>
            <p class="message">Not registered? <a href="register.php">Create an account</a></p>
            </form>
        </div>
    </div>

	<div class="php">
    <?php
    global $email;
    if (isset($_POST["button"])){
        $email = $_POST["email"];
        $pass = $_POST["pass"];
        if ((strpos($email, " ") != FALSE) or (strpos($pass, " ") != FALSE)) {
            echo "invalid entries (no spaces!)";
        } else {
            echo passthru("python Backend/Auth/Auth.py $email $pass");
        }
    } else {
        $email = "";
    }
    ?>
    </div>

    <script>
        function setName() {
            var name = '<?php global $email; passthru("python Backend/User/getName.py $email");?>';
            console.log(name);
            localStorage.setItem("NAME", name);
            return false;
        };
    </script>

</body>
</html>