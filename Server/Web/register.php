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

    <script>
      const login = () => window.location.replace("login.php");
    </script>

    <div class="register medium-text">
        <form action="" method="post" class="register">
            <table>
                <tr>
                    <td>Username:</td>
                    <td>
                        <input type="text" name="user">
                    </td>
                </tr>
                
                <tr>
                    <td>Email:</td>
                    <td>
                        <input type="email" name="email">
                    </td>
                </tr>

                <tr>
                    <td>Password:</td>
                    <td>
                        <input type="password" name="pass">
                    </td>
                </tr>

                <tr>
                    <input type="submit" name="submit" value="Register" onclick="login()">
                </tr>
            </table>
        </form>
    </div>
	
	<div class="php">
    <?php // Runs register.py to add login to file.
      if (isset($_POST["submit"])){
        $user = $_POST["user"];
        $pass = $_POST["pass"];
        $email = $_POST["email"];
        if ((strpos($user, " ") != FALSE) or (strpos($pass, " ") != FALSE) or (strpos($email, " ") != FALSE)) {
            echo "invalid entries (no spaces!)";
        } else {
            echo passthru("python Backend/Auth/Register.py $user $email $pass");
        }
      }
    ?>
    </div>

    <div class="row">
        <div class="column">
            <h2>Benefits of Pelican</h2>
            <p>Pelican is a community focused project that listens to the users unlike some larger apps. We focus on a user oriented experience that delievers both performance and accesibility! Pelican has regular updates that ensure the finest levels of security and we will always work out hardest to ensure you have a great time with out product.</p>
        </div>

        <div class="column">
            <h2>What makes us special</h2>
            <p>Pelican is made by the community for the community giving it a friendly feeling when compared to most corporate products *cough cough* discord. We focus on quality rather than pr and will always put the community first! We do this for fun and not for profit which means we will always go with what's best for Pelican and not what would produce the most money. We care for this project and we will do all we pelican to make this app the best it could possibly be!</p>
        </div>

        <div class="column">
            <h2>Want to donate?</h2>
            <p>If you ever want to donate you can send money to our team Patreon or KickStarter linked in the about tab. We aim to keep this project free from ads so any donations would be gladly appreciated.</p>
        </div>
    </div>
</body>