<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pelican</title>
    <link rel="stylesheet" href="css/Darkmode/welcome.css">
  </head>

  <body>
    <div class="container">
      <header>
        <h1 class="Motto">Its Time To Join Pelican</h1>
        <h4 class="Motto">With the security of Matrix and the ease of Discord</h4>
      </header>

      <div>
        <button onclick="login()">Login</button>
        <button onclick="register()">Register</button>
      </div>
    </div>
      
    <script>
      const login = () => window.location.replace("Login.php");
      const register = () => window.location.replace("Register.php");
    </script>
    </body>
</html>