<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pelican</title>
    <link rel="stylesheet" type="text/css" href="/css/styles.css">
    <link rel="shortcut icon" href="images/favicon.ico" />
  </head>
<body>

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

    <div class="container">
        <img src="images/logo.svg" alt="Pelican WebChat Logo">
      <header class="medium-text">
        <h1 class="motto">Its Time To Join Pelican</h1>
        <h4 class="motto">With the security of Matrix and the ease of Discord</h4>
      </header>
      <div>
        <button onclick="login()">Sign In</button>
        <button onclick="register()">Sign Up</button>
      </div>
    </div>
      
    <script>
      const login = () => window.location.replace("login.php");
      const register = () => window.location.replace("register.php");
    </script>
</body>
</html>
