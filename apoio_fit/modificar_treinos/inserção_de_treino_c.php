<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Insira novo treino</title>
</head>
<body>
<form action="cadastrando_treino_c.php" method="POST">
    <label for="tabela.php">Musculo</label>
    <input name = "musculo" value = ""  type="text">
    <br><br>
    <label for="">Exercício</label>
    <input name = "exercício"  type="text">
    <br><br>
    <label for="séries">Séries</label>
        <select name="séries">
            <option value="">Selecione</option>
            <option value="1">3</option>
            <option value="2">4</option>
            <option value="2">5</option>
        </select>
    <br><br>
    <label for="repetições">Repetições</label>
        <select name="repetições">
            <option value="">Selecione</option>
            <option value="1">8</option>
            <option value="2">12</option>
        </select>
    <br><br>
    <label for="intervalo">Intervalo</label>
        <select name="intervalo">
            <option value="">Selecione</option>
            <option value="00:01:00">00:01:00</option>
            <option value="00:01:30">00:01:30</option>
        </select>
    <br><br>
    <button type="submit">Salvar</button> 
    <br><br>
    <a href="../treino.php">Voltar para tabela</a>
</body>
</html>