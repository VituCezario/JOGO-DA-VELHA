<?php 
include('conexão.php');
if (!isset($_SESSION)) {
    session_start();
}
$musculo = $_POST['musculo'];
$exercicio = $_POST['exercício'];
$séries = $_POST['séries'];
$repetições = $_POST['repetições'];
$intervalo = $_POST['intervalo'];

$sql = "INSERT INTO treino_b VALUES (DEFAULT, '$musculo', '$exercicio', '$séries', '$repetições', '$intervalo')";
$retorno = $mysqli->query($sql);
mysqli_close($mysqli);
echo "Treino adicionado!";
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <a href="../adm.php">Voltar para tabela</a>
</body>
</html>