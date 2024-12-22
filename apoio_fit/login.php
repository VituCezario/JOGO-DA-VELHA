<?php 
include('conexão.php');

if(isset($_POST['email']) || isset($_POST['senha'])) {
    if(strlen($_POST['email']) == 0){
        echo "Preencha seu email";
    }else if(strlen($_POST['senha']) == 0){
        echo "Preencha sua senha";
    } else {
        $email = $mysqli->real_escape_string($_POST['email']);
        $senha = $mysqli->real_escape_string($_POST['senha']);
        

        $sql_code =  "SELECT * FROM login WHERE email = '$email' AND senha = '$senha'";
        $sql_query = $mysqli->query($sql_code) or die("Falha na execução do código MySQL: " . $mysqli->error);
    
        $quantidade = $sql_query->num_rows;
    
        if ($quantidade == 1) {
            $usuario = $sql_query->fetch_assoc();

            if (!isset($_SESSION)) {
                session_start();
            }
            $_SESSION['user'] = $usuario['id'];
            $_SESSION['nome'] = $usuario['nome'];
            $_SESSION['ativa'] = TRUE;
            if($usuario['id'] == '6'){
                header("Location: adm.php");
            }elseif($usuario['id'] != '6'){
                header("Location: cad.php");

            }

        } else {
            echo "Falha ao logar! Email ou Senha incorretos";
        }
    }
}
?>


<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LOGIN</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header> 
        <h1> Acesse sua conta </h1>
    </header>
    <section>
        <form action="", method="POST">
            <label for="email">Email</label>
            <input type="text" name="email" id="idnome" required="obrigatório">
            <label for="senha">Senha</label>
            <input type="password" name="senha" id="idsenha" required="obrigatório">
            <button type="submit">Entrar</button>
    </section>
    </form> 

</body>
</html>