<?php 
include("conexão.php");
if (!isset($_SESSION)) {
    session_start();
}
?>


<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Atualize seu treino</title>
    <link rel="stylesheet" href="../formulario.css">
</head>
<body>
    <?php if(isset($_GET['id_c'])) { 
        $ordem = $_GET['id_c'];
        $treino = buscaUnica_c($mysqli, "treino_c", $ordem);
        
        ?>
        <div>
            <h1 id="titulo">Editando o exercício <?php echo $_GET['exercício'] ?>!</h1>
        </div>
    <?php update_treino_c($mysqli); } ?>

    <fieldset class="grupo">
        <form action="" method="POST">
        <input name = "ordem"  type="hidden" value="<?php echo $treino['id_c']?>">
        <br><br>
        <label for="tabela.php">Musculo</label>
        <input name = "musculo" value = "<?php echo $treino['musculo']?>"  type="text">
        <br><br>
        <label for="">Exercício</label>
        <input name = "exercício"  type="text" value="<?php echo $treino['exercício']?>">
    </fieldset>
    <br>
    <div class="campo">
        <label for="séries">Séries</label>
            <select name="séries">
                <option value="<?php echo $treino['séries'] ?>"><?php echo $treino['séries'] ?></option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
            </select>
    </div>
    <br>
    <div class="campo">
        <label for="repetições">Repetições</label>
            <select name="repetições">
                <option value="<?php echo $treino['repetições'] ?>"><?php echo $treino['repetições'] ?></option>
                <option value="8">8</option>
                <option value="12">12</option>
            </select>
    </div>
    <br>
    <div class="campo">
        <label for="intervalo">Intervalo</label>
            <select name="intervalo">
                <option value="<?php echo $treino['intervalo'] ?>"><?php echo $treino['intervalo'] ?></option>
                <option value="00:01:00">00:01:00</option>
                <option value="00:01:30">00:01:30</option>
            </select>
    </div>

    <br><br>
    <button type="submit" name="atualizar">Salvar</button> 
    <br><br>
    <a href="../treino.php">Voltar para tabela</a>
</body>
</html>