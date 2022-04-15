<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" type="text/css" href="/css/Darkmode/styles.css">
        <link rel="shortcut icon" href="images/favicon.ico" />
        <title>Pelican</title>
    </head>
    <body>
        <script>
            window.onload = event => {
                document.getElementById("username-display").innerHTML = localStorage.getItem("NAME");
            };
        </script>
        <div class="topnav">
            <a href="home.php">Home</a>
            <a href="download.php">Download</a>
            <a href="support.php">Support</a>
            <a href="about.php">About</a>
            <a href="login.php">Login</a>
            <a href="register.php">Register</a>
            <a href="tos.php">ToS</a>
            <a href="profile.php">Profile</a>
            <p id="username-display"  class="pos-right"></p>
        </div>
        <div class="row medium-text">
            <div class="column">
                <h3>Downloads</h3>
                <p>Windows x64 <a href="https://www.google.com">
                        <br>
                        <img class="pos-left" src="images/windows.png" alt="Windows Icon">
                    </a>
                </p>
                <p>
                    <br>
                    <br>Windows x86 <a href="https://www.google.com">
                        <br>
                        <img class="pos-left" src="images/windows.png" alt="Windows Icon">
                    </a>
                </p>
                <p>
                    <br>
                    <br>MacBook <a href="https://www.google.com">
                        <br>
                        <img class="pos-left" src="images/apple.png" alt="Windows Icon">
                    </a>
                </p>
            </div>
            <div class="column">
                <h3>Linux Downloads</h3>
                <p>Linux <a href="https://www.google.com">
                        <br>
                        <img class="pos-left" src="images/linux.png" alt="Windows Icon">
                    </a>
                </p>
            </div>
        </div>
    </body>