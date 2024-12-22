<?php 
$usuario = 'root';
$senha = '';
$database = 'apoio_fit';
$host = 'localhost';

$mysqli =  new mysqli($host,$usuario,$senha,$database);
if ($mysqli->error){
    die("Falha ao conectar ao banco de dados");
}

function buscaUnica_s($mysqli, $tabela, $ordem){
    $query = "SELECT * FROM $tabela WHERE ordem_s =" . (int) $ordem;
    $execute = $mysqli->query($query);
    $resultado = $execute->fetch_assoc();
    return $resultado;

}

function buscaUnica_a($mysqli, $tabela, $ordem){
    $query = "SELECT * FROM $tabela WHERE id_a =" . (int) $ordem;
    $execute = $mysqli->query($query);
    $resultado = $execute->fetch_assoc();
    return $resultado;
}

function buscaUnica_b($mysqli, $tabela, $ordem){
    $query = "SELECT * FROM $tabela WHERE id_b =" . (int) $ordem;
    $execute = $mysqli->query($query);
    $resultado = $execute->fetch_assoc();
    return $resultado;
}

function buscaUnica_c($mysqli, $tabela, $ordem){
    $query = "SELECT * FROM $tabela WHERE id_c =" . (int) $ordem;
    $execute = $mysqli->query($query);
    $resultado = $execute->fetch_assoc();
    return $resultado;
}

function update_suplemtento($mysqli){
    if(isset($_POST['atualizar'])){

        $suplemento = $_POST['suplemento'];
        $o_que_é = $_POST['o_que_é'];
        $descrição = $_POST['descrição'];
        $ordem = $_POST['ordem_s'];

        $query = "UPDATE suplementos_alimentares SET suplemento = '$suplemento',  o_que_é = '$o_que_é', descrição = '$descrição' WHERE ordem_s =" . (int) $ordem;
        
    $execute = $mysqli->query($query);
        if($execute) {
            echo "Treino atualizado com sucesso!";
        } else{
            echo "Erro na atualização!";
        }
    }

}

function update_treino_a($mysqli){
    if(isset($_POST['atualizar'])){

        $musculo = $_POST['musculo'];
        $exercício = $_POST['exercício'];
        $séries = $_POST['séries'];
        $repetições = $_POST['repetições'];
        $intervalo = $_POST['intervalo'];
        $ordem = $_POST['ordem'];

        $query = "UPDATE treino_a SET musculo = '$musculo',  exercício = '$exercício', séries = '$séries', repetições = '$repetições', intervalo = '$intervalo' WHERE id_a =" . (int) $ordem;
        
    $execute = $mysqli->query($query);
        if($execute) {
            echo "Treino atualizado com sucesso!";
        } else{
            echo "Erro na atualização!";
        }
    }

}

function update_treino_b($mysqli){
    if(isset($_POST['atualizar'])){

        $musculo = $_POST['musculo'];
        $exercício = $_POST['exercício'];
        $séries = $_POST['séries'];
        $repetições = $_POST['repetições'];
        $intervalo = $_POST['intervalo'];
        $ordem = $_POST['ordem'];

        $query = "UPDATE treino_b SET musculo = '$musculo',  exercício = '$exercício', séries = '$séries', repetições = '$repetições', intervalo = '$intervalo' WHERE id_b =" . (int) $ordem;
        
    $execute = $mysqli->query($query);
        if($execute) {
            echo "Treino atualizado com sucesso!";
        } else{
            echo "Erro na atualização!";
        }
    }

}
function update_treino_c($mysqli){
    if(isset($_POST['atualizar'])){

        $musculo = $_POST['musculo'];
        $exercício = $_POST['exercício'];
        $séries = $_POST['séries'];
        $repetições = $_POST['repetições'];
        $intervalo = $_POST['intervalo'];
        $ordem = $_POST['ordem'];

        $query = "UPDATE treino_c SET musculo = '$musculo',  exercício = '$exercício', séries = '$séries', repetições = '$repetições', intervalo = '$intervalo' WHERE id_c =" . (int) $ordem;
        
    $execute = $mysqli->query($query);
        if($execute) {
            echo "Treino atualizado com sucesso!";
        } else{
            echo "Erro na atualização!";
        }
    }

}

?>

