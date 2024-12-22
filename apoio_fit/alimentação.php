<?php 
    include('conexão.php');
    if (!isset($_SESSION)) {
        session_start();
    }
    $id =  $_SESSION['user'];

    $sql_cafe = "SELECT login.nome, café_da_manhã.*  FROM login join café_da_manhã on café_da_manhã.opções = login.opção_de_café_da_manhã
    WHERE login.id = '$id';";

    $sql_lanche = "SELECT login.nome, lanche.* 
    FROM login join lanche
    on lanche.opção_lanche = login.opção_de_lanche
    WHERE login.id = '$id';";

    $mysqli_cafe= $mysqli->query($sql_cafe);
    $mysqli_lanche= $mysqli->query($sql_lanche);
    // $mysqli_lanche= $mysqli->query($sql_lanche);
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SUGESTÕES DE REFEIÇÕES</title>
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

     <table>
        <thead>
            <h2 id="subtitulo1">Café da Manhã</h2>
            <caption>Sugestão</caption>
            <tr>
                <th>Nome</th>
                <th>Opções</th>
                <th>Alimento</th>
                <th>Quantidade</th>
                <th>Alimento</th>
                <th>Quantidade</th>
                <th>Alimento</th>
                <th>Quantidade</th>
                <th>Alimento</th>
                <th>Quantidade</th>
                <th>Alimento</th>
                <th>Quantidade</th>
            </tr>
        </thead>
            <?php while($dado =  $mysqli_cafe->fetch_array()){?>
                    <tbody>
                        <tr>
                            <td><?php echo $dado["nome"]?></td>
                            <td><?php echo $dado["opções"]?></td>
                            <td><?php echo $dado["1_alimento"]?></td>
                            <td><?php echo $dado["quantidade1"]?></td>
                            <td><?php echo $dado["2_alimento"]?></td>
                            <td><?php echo $dado["quantidade2"]?></td>
                            <td><?php echo $dado["3_alimento"]?></td>
                            <td><?php echo $dado["quantidade3"]?></td>
                            <td><?php echo $dado["4_alimento"]?></td>
                            <td><?php echo $dado["quantidade4"]?></td>
                            <td><?php echo $dado["5_alimento"]?></td>
                            <td><?php echo $dado["quantidade5"]?></td>
                        </tr>
                    </tbody>
             <?php } ?>
    </table>

    <table>
        <thead>
            <h2 id="subtitulo1">Lanche</h2>
            <caption>Sugestão</caption>
            <tr>
                <th>Nome</th>
                <th>Opções</th>
                <th>Alimento</th>
                <th>Quantidade</th>
                <th>Alimento</th>
                <th>Quantidade</th>
                <th>Alimento</th>
                <th>Quantidade</th>
            </tr>
        </thead>
            <?php while($dado_lanche =  $mysqli_lanche->fetch_array()){?>
                    <tbody>
                        <tr>
                            <td><?php echo $dado_lanche["nome"]?></td>
                            <td><?php echo $dado_lanche["opção_lanche"]?></td>
                            <td><?php echo $dado_lanche["1_alimento"]?></td>
                            <td><?php echo $dado_lanche["quantidade1"]?></td>
                            <td><?php echo $dado_lanche["2_alimento"]?></td>
                            <td><?php echo $dado_lanche["quantidade2"]?></td>
                            <td><?php echo $dado_lanche["3_alimento"]?></td>
                            <td><?php echo $dado_lanche["quantidade3"]?></td>
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