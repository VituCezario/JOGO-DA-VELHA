<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Insira novo suplemento</title>
</head>
<body>
<form action="cadastrando_suplemento.php" method="POST">
    <label for="suplemento">Suplemento</label>
    <input name = "suplemento" value = ""  type="text">
    <br><br>
    <label for="">O que é?</label>
    <input name = "o_que_é"  type="text">
    <br><br>
    <label for="descrição"><strong>Descrição: </strong></label>
        <textarea rows="6" style="width: 26em" id="descrição" name="descrição"></textarea>
    <br><br>
    <button type="submit">Salvar</button> 
    <br><br>
    <a href="../suplementos.php">Voltar para tabela</a>
</body>
</html>
