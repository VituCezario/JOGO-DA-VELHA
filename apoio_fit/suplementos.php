<?php 
    include('conexão.php');
    if (!isset($_SESSION)) {
        session_start();
    }
    $sql = "SELECT * from suplementos_alimentares";
    $mysqli_s= $mysqli->query($sql);

?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Suplementos</title>
    <style>
        table td, table th {
            border: 1px solid #ccc;
            padding: 5px;
        }

        table {
            border-collapse: collapse;
            width: 100%;
        }

        table th {
            background-color: #ddd;
        }
        .tabela-um {
            max-width: 100%;
            overflow-x: auto;
        }
        #titulo{
            text-align: center;
        }
        #subtitulo1, #subtitulo2, #subtitulo3{
            text-align: center;
            background-color: aquamarine;
            margin-bottom: 2px;
        }
        table caption{
            margin-bottom: 4px;
        }
    </style>
</head>
<body>
    <?php  if (isset($_SESSION['ativa'])){ ?>

    <?php 
    if(isset($_GET['ordem_s'])){ ?>
        <h2>Tem certeza que deseja deletar o exercício <?php echo $_GET['suplemento']; ?>?</h2>
        <form action="" method="post">
            <input type="hidden" name="ordem_s" value="<?php echo $_GET['ordem_s']; ?>">
            <input type="submit" value="Deletar" name="deletar">
        </form>
    <?php } ?>

    <?php if(isset($_POST['ordem_s'])){
        deletar_s($mysqli, "suplementos_alimentares", $_POST['ordem_s']);
        }
    ?>

    <table>
    <thead>
        <h2 id="subtitulo1">SUPLEMENTOS</h2>
        <caption>SUGESTÕES</caption>
        <tr>
            <th>Suplemento</th>
            <th>O que é?</th>
            <th>Descrição</th>

        </tr>
    </thead>
    <?php while($dado = $mysqli_s->fetch_array()){?>
                <tbody>
                    <tr>
                        <td><?php echo $dado["suplemento"]?></td>
                        <td><?php echo $dado["o_que_é"]?></td>
                        <td><?php echo $dado["descrição"]?></td>
                    </tr>
                </tbody>
         <?php } ?>
    </table>
    <br><br>
    <p><a href="cad.php">Volta para a página anterior</a></p>
    <?php mysqli_close($mysqli);?>
    <?php 
    } else {
        header( "Location: login.php");
    }
    ?>
</body>
</html>