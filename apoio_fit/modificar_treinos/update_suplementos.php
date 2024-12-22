<?php 
include("conexão.php");
if (!isset($_SESSION)) {
    session_start();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php if(isset($_GET['ordem_s'])) { 
            $ordem = $_GET['ordem_s'];
            $suplementos = buscaUnica_s($mysqli, "suplementos_alimentares", $ordem);
            update_suplemtento($mysqli);
            ?>
            <h2>Editando o suplemento <?php echo $_GET['suplemento'] ?>.</h2>
    <?php } ?>
    <form action="" method="POST">
    <label for="">Ordem</label>
    <input name = "ordem_s"  type="hidden" value="<?php echo $suplementos['ordem_s']?>">
    <br><br>
    <label for="suplemento">Suplemento</label>
    <input name = "suplemento" value = "<?php echo $suplementos['suplemento']?>"  type="text">
    <br><br>
    <label for="">O que é?</label>
    <input name = "o_que_é" value="<?php echo $suplementos['o_que_é']?>" type="text">
    <br><br>
    <label for="descrição"><strong>Descrição: </strong></label>
        <textarea rows="6" style="width: 26em" id="descrição" name="descrição" ></textarea>
    <br><br>
    <button type="submit" name="atualizar">Salvar</button> 
    <br><br>
    <a href="../suplementos.php">Voltar para tabela</a>

</body>
</html>