<?php 
include('conexão.php');
?>


<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tela de inicio</title>
</head>
<body>
    <?php  if (isset($_SESSION['ativa'])){ ?>

    <header>
        <h1>INICIO</h1>
        <main>
        <a href="suplementos.php">SUPLEMENTAÇÃO</a>
        <br><br>
        <a href="alimentação.php">ALIMENTAÇÃO</a>
        <br><br>
        <a href="treino.php">TREINO</a>
        </main>
        <p><a href="logout.php">Sair</a></p>
    </header>

    <?php 
    } else {
        header( "Location: login.php");
    }
    ?>
</body>
</html>