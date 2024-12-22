<?php 
    include('conexão.php');
    if (!isset($_SESSION)) {
        session_start();
    }
    $sql = "SELECT * from suplementos_alimentares";
    $mysqli_s= $mysqli->query($sql);

    $sql_a = "SELECT * FROM treino_a";
    
    $sql_b = "SELECT * FROM treino_b";
    
    $sql_c = "SELECT * FROM treino_c";
    $mysqli_a= $mysqli->query($sql_a);
    $mysqli_b= $mysqli->query($sql_b);
    $mysqli_c= $mysqli->query($sql_c);

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
        <h2>Tem certeza que deseja deletar o suplemento <?php echo $_GET['suplemento']; ?>?</h2>
        <form action="" method="post">
            <input type="hidden" name="ordem_s" value="<?php echo $_GET['ordem_s']; ?>">
            <input type="submit" value="Deletar" name="deletar">
        </form>
    <?php } ?>

    <?php if(isset($_POST['ordem_s'])){
        deletar_s($mysqli, "suplementos_alimentares", $_POST['ordem_s']);
        header("Location: adm.php");
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
            <th>Ação</th>
        </tr>
    </thead>
    <?php while($dado = $mysqli_s->fetch_array()){?>
                <tbody>
                    <tr>
                        <td><?php echo $dado["suplemento"]?></td>
                        <td><?php echo $dado["o_que_é"]?></td>
                        <td><?php echo $dado["descrição"]?></td>
                        <td>
                            <a href="adm.php?ordem_s=<?php echo $dado["ordem_s"];  ?> &suplemento=<?php echo $dado["suplemento"];?>">Excluir</a>
                            |
                            <a href="modificar_treinos/update_suplementos.php?ordem_s=<?php echo $dado["ordem_s"];  ?> &suplemento=<?php echo $dado["suplemento"];?>">Editar</a>
                        </td>
                    </tr>
                </tbody>
         <?php } ?>
    </table>
    <br><br>
    <a href="modificar_treinos/inserção_de_suplementação.php">Inserir novo suplemento</a>
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
                <th>Ação</th>
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
                            <td>
                                <a href="modificar_treinos/update_de_treino_a.php?id_a=<?php echo $dado["id_a"];  ?> &exercício=<?php echo $dado["exercício"];?>">Editar</a>
                            </td>
                        </tr>
                    </tbody>
             <?php } ?>
    </table>
    <br><br>
    <a href="modificar_treinos/inserção_de_treino_a.php">Inserir novo treino</a>
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
                <th>Ação</th>
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
                            <td>
                                <a href="modificar_treinos/update_de_treino_b.php?id_b=<?php echo $dado_b["id_b"];  ?> &exercício=<?php echo $dado_b["exercício"];?>">Editar</a>
                            </td>
                        </tr>
                    </tbody>
             <?php } ?>
    </table>
    <br><br>
    <a href="modificar_treinos/inserção_de_treino_b.php">Inserir novo treino</a>
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
                <th>Ação</th>
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
                            <td>
                                <a href="modificar_treinos/update_de_treino_c.php?id_c=<?php echo $dado_c["id_c"];  ?> &exercício=<?php echo $dado_c["exercício"];?>">Editar</a>
                            </td>
                        </tr>
                    </tbody>
             <?php } ?>
    </table>

    <a href="modificar_treinos/inserção_de_suplementação.php">Inserir novo treino</a>
    <br><br>
    </main>
    <p><a href="logout.php">Sair</a></p>
    </header>

    <p><a href="cad.php">Volta para a página anterior</a></p>
    <?php mysqli_close($mysqli);?>
    <?php 
    } else {
        header( "Location: login.php");
    }
    ?>
</body>
</html>