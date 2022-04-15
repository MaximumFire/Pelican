<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" type="text/css" href="css/main.css">
        <title>Main User Page</title>
    </head>

    <body>
        <div class="sidenav">
            <a href="search.php">Add Friend</a>
        </div>


        <div class="theform"> 
            <form action="" method="post">
                <input type="text" name="nametag" placeholder="Username:Tag">
                <button name="button">Search</button>
            </form>
        </div>

        <div class="php">
            <?php 
            if (isset($_POST['button'])) {
                $searchuser = $_POST["nametag"];
                if ((strpos($searchuser, " ") != FALSE)) {
                    echo "invalid entries (no spaces!)";
                } else {
                    echo passthru("python ../../Backend/User/SearchUser.py $searchuser");
                }
            }
            ?>
        </div>
    </body>
</html>