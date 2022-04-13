<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="/css/styles.css">
    <link rel="shortcut icon" href="images/favicon.ico" />
    <title>Pelican</title>
</head>
<body>

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

    </div>

    <div class="login medium-text">
        <form action="" method="post" class="login">
            <table>
                <tr>
                    <td>Email:</td>
                    <td>
                        <input type="text" name="email">
                    </td>
                </tr>

                <tr>
                    <td>Password:</td>
                    <td>
                        <input type="password" name="pass">
                    </td>
                </tr>

                <tr>
                    <input type="submit" name="submit" value="Login">
                </tr>
            </table>
        </form>
    </div>
	
	<div class="php">
    <?php
      if (isset($_POST["submit"])){
        $user = "0";
        $email = $_POST["email"];
        $pass = $_POST["pass"];
        $userid = "0";
        if ((strpos($user, " ") != FALSE) or (strpos($pass, " ") != FALSE)) {
            echo "invalid entries (no spaces!)";
        } else {
            echo passthru("python Backend/Auth/Auth.py $user $email $pass $userid");
        }
      }
    ?>
    </div>

</body>
</html>