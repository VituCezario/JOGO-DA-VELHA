<?php 
$usuario = 'root';
$senha = '';
$database = 'apoio_fit';
$host = 'localhost';

$mysqli =  new mysqli($host,$usuario,$senha,$database);
if ($mysqli->error){
    die("Falha ao conectar ao banco de dados");
}

if (!isset($_SESSION)) {
    session_start();
}

else if (!isset($_SESSION['id'])) {
    die ("Você não pode acessar essa página porque não está logado.<p><a href=\"login.php\">Entrar</a></p>");
};

function deletar_s($mysqli, $tabela, $ordem){
    if(!empty($ordem)){
        $query = "DELETE FROM $tabela WHERE ordem_s =". (int) $ordem;
        $execute = $mysqli->query($query);
        if($execute) {
            echo "Suplemento deletado com sucesso!";
        } else{
            echo "Erro ao deletar!";
        }
    }
    
}



?>

