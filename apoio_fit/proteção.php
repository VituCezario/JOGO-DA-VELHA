<?php 
if (!isset($_SESSION)) {
    session_start();
}

else if (!isset($_SESSION['id'])) {
    die ("Você não pode acessar essa página porque não está logado.<p><a href=\"login.php\">Entrar</a></p>");
};

?>