<?php 
    if(isset($_GET['id_a'])){ ?>
        <h2>Tem certeza que deseja deletar o exercício <?php echo $_GET['exercício']; ?>?</h2>
        <form action="" method="post">
            <input type="hidden" name="id_a" value="<?php echo $_GET['id_a']; ?>">
            <input type="submit" value="Deletar" name="deletar">
        </form>
    <?php } ?>

    <?php if(isset($_POST['id_a'])){
        deletar_a($mysqli, "treino_a", $_POST['id_a']);
        header( "Location: treino.php");
        }
    ?>

    <?php 
    if(isset($_GET['id_b'])){ ?>
        <h2>Tem certeza que deseja deletar o exercício <?php echo $_GET['exercício']; ?>?</h2>
        <form action="" method="post">
            <input type="hidden" name="id_b" value="<?php echo $_GET['id_b']; ?>">
            <input type="submit" value="Deletar" name="deletar">
        </form>
    <?php } ?>

    <?php if(isset($_POST['id_b'])){
        deletar_b($mysqli, "treino_b", $_POST['id_b']);
        header( "Location: treino.php");
        }
    ?>
    
    <?php 
    if(isset($_GET['id_c'])){ ?>
        <h2>Tem certeza que deseja deletar o exercício <?php echo $_GET['exercício']; ?>?</h2>
        <form action="" method="post">
            <input type="hidden" name="id_c" value="<?php echo $_GET['id_c']; ?>">
            <input type="submit" value="Deletar" name="deletar">
        </form>
    <?php } ?>

    <?php if(isset($_POST['id_c'])){
        deletar_c($mysqli, "treino_c", $_POST['id_c']);
        header( "Location: treino.php");
        }
    ?>

<!-- <a href="treino.php?id_a=<?php echo $dado["id_a"];  ?> &exercício=<?php echo $dado["exercício"];?>">Excluir</a> -->

    