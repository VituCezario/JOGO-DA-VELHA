<?php 
include('conexão.php');
if (!isset($_SESSION)) {
    session_start();
}
$suplemento = $_POST['suplemento'];
$o_que_é = $_POST['o_que_é'];
$descrição = $_POST['descrição'];


$sql = "INSERT INTO suplementos_alimentares VALUES (DEFAULT, '$suplemento', '$o_que_é', '$descrição')";
$retorno = $mysqli->query($sql);
mysqli_close($mysqli);
echo "Suplemento adicionado!";
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
</head>
<body>
    <a href="../adm.php">Voltar para tabela</a>
</body>
</html>