<?php 
    include('conexão.php');
    if (!isset($_SESSION)) {
        session_start();
    }
    $id = $_SESSION['user'];

    $sql_a = "select l.nome, t_a.id_a, t_a.musculo, t_a.exercício, t_a.séries, t_a.repetições, t_a.intervalo from login as l
    join treinar_a as treinar
    on l.id = treinar.id_login
    join treino_a as t_a
    on treinar.id_treino = t_a.id_a
    WHERE l.id = '$id'
    order by treinar.id_treina;";
    
    $sql_b = "select l.nome, t_b.id_b, t_b.musculo, t_b.exercício, t_b.séries, t_b.repetições, t_b.intervalo from login as l
    join treinar_b as treinar
    on l.id = treinar.id_login
    join treino_b as t_b
    on treinar.id_treino = t_b.id_b
    WHERE l.id = '$id'
    order by treinar.id_treina;";
    
    $sql_c = "select l.nome, t_c.id_c, t_c.musculo, t_c.exercício, t_c.séries, t_c.repetições, t_c.intervalo from login as l
    join treinar_c as treinar
    on l.id = treinar.id_login
    join treino_c as t_c
    on treinar.id_treino = t_c.id_c
    WHERE l.id = '$id'
    order by treinar.id_treina;";
    $mysqli_a= $mysqli->query($sql_a);
    $mysqli_b= $mysqli->query($sql_b);
    $mysqli_c= $mysqli->query($sql_c);
?>


<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TABELA FIT</title>
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

    <h1 id="titulo"> Divisão de Treino</h1>

    
    <table>
        <thead>
            <h2 id="subtitulo1">Treino A</h2>
            <caption>Peitoral + Tríceps + Abdomen</caption>
            <tr>
                <th>Musculo</th>
                <th>Exercício</th>
                <th>Séries</th>
                <th>Repetições</th>
                <th>Intervalo</th>
            </tr>
        </thead>
            <?php while($dado = $mysqli_a->fetch_array()){?>
                    <tbody>
                        <tr>
                            <td><?php echo $dado["musculo"]?></td>
                            <td><?php echo $dado["exercício"]?></td>
                            <td><?php echo $dado["séries"]?></td>
                            <td><?php echo $dado["repetições"]?></td>
                            <td><?php echo $dado["intervalo"]?></td>
                        </tr>
                    </tbody>
             <?php } ?>
    </table>
    <br><br>
    <table>
        <thead>
            <h2 id="subtitulo1">Treino B</h2>
            <caption>Costas + Bíceps + Lomba</caption>
            <tr>
                <th>Musculo</th>
                <th>Exercício</th>
                <th>Séries</th>
                <th>Repetições</th>
                <th>Intervalo</th>
            </tr>
        </thead>
            <?php while($dado_b = $mysqli_b->fetch_array()){?>
                    <tbody>
                        <tr>
                            <td><?php echo $dado_b["musculo"]?></td>
                            <td><?php echo $dado_b["exercício"]?></td>
                            <td><?php echo $dado_b["séries"]?></td>
                            <td><?php echo $dado_b["repetições"]?></td>
                            <td><?php echo $dado_b["intervalo"]?></td>
                        </tr>
                    </tbody>
             <?php } ?>
    </table>
    <br><br>
    <table>
        <thead>
            <h2 id="subtitulo1">Treino C</h2>
            <caption>Peitoral + Tríceps + Abdomen</caption>
            <tr>
                <th>Musculo</th>
                <th>Exercício</th>
                <th>Séries</th>
                <th>Repetições</th>
                <th>Intervalo</th>
            </tr>
        </thead>
            <?php while($dado_c = $mysqli_c->fetch_array()){?>
                    <tbody>
                        <tr>
                            <td><?php echo $dado_c["musculo"]?></td>
                            <td><?php echo $dado_c["exercício"]?></td>
                            <td><?php echo $dado_c["séries"]?></td>
                            <td><?php echo $dado_c["repetições"]?></td>
                            <td><?php echo $dado_c["intervalo"]?></td>
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