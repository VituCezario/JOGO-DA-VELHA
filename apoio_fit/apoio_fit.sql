CREATE DATABASE  IF NOT EXISTS `apoio_fit` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci */;
USE `apoio_fit`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: apoio_fit
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.28-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `café_da_manhã`
--

DROP TABLE IF EXISTS `café_da_manhã`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `café_da_manhã` (
  `opções` tinyint(4) NOT NULL AUTO_INCREMENT,
  `1_alimento` varchar(40) NOT NULL,
  `quantidade1` varchar(40) NOT NULL,
  `2_alimento` varchar(40) NOT NULL,
  `quantidade2` varchar(40) NOT NULL,
  `3_alimento` varchar(40) NOT NULL,
  `quantidade3` varchar(40) NOT NULL,
  `4_alimento` varchar(40) DEFAULT NULL,
  `quantidade4` varchar(40) DEFAULT NULL,
  `5_alimento` varchar(40) DEFAULT NULL,
  `quantidade5` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`opções`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `café_da_manhã`
--

LOCK TABLES `café_da_manhã` WRITE;
/*!40000 ALTER TABLE `café_da_manhã` DISABLE KEYS */;
INSERT INTO `café_da_manhã` VALUES (1,'Café com leite ','300 ml (100 de café e 200 de leite)','Pão Francês','até 50 gramas','Azeite','1 colher de chá','Queijo Branco','1 fatia','Melão','160 gramas'),(2,'Café com leite ','300 ml (100 de café e 200 de leite)','Pão Francês','até 50 gramas','Azeite','1 colher de chá','Queijo Branco','1 fatia','Maçã','140 gramas'),(3,'Café com leite ','300 ml (100 de café e 200 de leite)','Tapioca','Duas de até 125 grama cada','Reiqueijão','2 colher de sopa','Queijo Branco','1 fatia','Maçã','140 gramas'),(4,'Café com leite ','300 ml (100 de café e 200 de leite)','Tapioca','Duas de até 125 grama cada','Geléia','2 colher de sopa','Melão','160 gramas','',''),(5,'Iorgute','170 gramas','Pão Francês','até 50 gramas','Azeite','1 colher de chá','Peito de peru','2 fatia','Melão','160 gramas'),(6,'Iorgute','170 gramas','Pão Francês','até 50 gramas','Azeite','1 colher de chá','Peito de peru','2 fatia','Maçã','140 gramas');
/*!40000 ALTER TABLE `café_da_manhã` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lanche`
--

DROP TABLE IF EXISTS `lanche`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lanche` (
  `opção_lanche` tinyint(11) NOT NULL AUTO_INCREMENT,
  `1_alimento` varchar(40) NOT NULL,
  `quantidade1` varchar(40) NOT NULL,
  `2_alimento` varchar(40) NOT NULL,
  `quantidade2` varchar(40) NOT NULL,
  `3_alimento` varchar(40) NOT NULL,
  `quantidade3` varchar(40) NOT NULL,
  PRIMARY KEY (`opção_lanche`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lanche`
--

LOCK TABLES `lanche` WRITE;
/*!40000 ALTER TABLE `lanche` DISABLE KEYS */;
INSERT INTO `lanche` VALUES (1,'Salada de frutas','450 gramas','Mel','1 colher de sopá','Suco natural','450 ml'),(2,'Salada de frutas','450 gramas','Mix de castanhas','1 colher de sopá','Suco natural','450 ml'),(3,'Bolacha Salgada','4 unidades','Mamão papaya','135 gramas','Suco natural','450 ml'),(4,'Bolacha Salgada','4 unidades','Pêra','90 gramas','Suco natural','450 ml'),(5,'Sanduíche natural','1 unidades','Manga','130 gramas','Suco natural','450 ml'),(6,'Sanduíche natural','1 unidades','Pêra','90 gramas','Suco natural','450 ml');
/*!40000 ALTER TABLE `lanche` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(140) NOT NULL,
  `senha` varchar(16) NOT NULL,
  `nome` varchar(40) NOT NULL,
  `opção_de_café_da_manhã` tinyint(11) DEFAULT NULL,
  `opção_de_lanche` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `opção_de_café_da_manhã` (`opção_de_café_da_manhã`),
  KEY `opção_de_lanche` (`opção_de_lanche`),
  CONSTRAINT `login_ibfk_1` FOREIGN KEY (`opção_de_café_da_manhã`) REFERENCES `café_da_manhã` (`opções`),
  CONSTRAINT `login_ibfk_2` FOREIGN KEY (`opção_de_lanche`) REFERENCES `lanche` (`opção_lanche`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES (1,'andreirodrigues@unicid.com','barros','Andrei Rodrigues de Barros',2,2),(2,'angeladias@unicid.com','caruso','Angela Dias Caruso',5,6),(3,'kailanedesihe@unicid.com ','goncalves','Kailane Desihe Silva Gonçalves ',3,1),(4,'victoralves@unicid.com','santos','Victor Alves Souza dos Santos',1,5),(5,'vitormedeiros@unicid.com','cezario','Vitor de Medeiros Cezario',6,4),(6,'cidadm@unicid.com','cid123','Adm Cid',1,1);
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suplementos_alimentares`
--

DROP TABLE IF EXISTS `suplementos_alimentares`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suplementos_alimentares` (
  `ordem_s` tinyint(4) NOT NULL AUTO_INCREMENT,
  `suplemento` varchar(35) NOT NULL,
  `o_que_é` tinytext NOT NULL,
  `descrição` text NOT NULL,
  PRIMARY KEY (`ordem_s`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suplementos_alimentares`
--

LOCK TABLES `suplementos_alimentares` WRITE;
/*!40000 ALTER TABLE `suplementos_alimentares` DISABLE KEYS */;
INSERT INTO `suplementos_alimentares` VALUES (1,'Whey protein','Proteína encontrada no leite','Ele fornece ao corpo uma alta quantidade de proteínas e aminoácidos que ajudam a impulsionar o processo anabólico. É absorvido rapidamente pelo organismo. O que significa que fornece uma fonte essencial e rápida de construção muscular e melhora o processo de recuperação pós-treino.'),(4,'Creatina','Glicina, arginina e metionina','A creatina é uma molécula encontrada naturalmente no tecido muscular, em quantidade limitada, que participa de todos os processos energéticos do corpo. Ela é fundamental na contração muscular, proporcionando maior força muscular, resistência física, redução no tempo de recuperação, e aumento do volume muscular.\r\n');
/*!40000 ALTER TABLE `suplementos_alimentares` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `treinar_a`
--

DROP TABLE IF EXISTS `treinar_a`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `treinar_a` (
  `id_treina` int(11) NOT NULL AUTO_INCREMENT,
  `id_login` int(11) DEFAULT NULL,
  `id_treino` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_treina`),
  KEY `id_login` (`id_login`),
  KEY `id_treino` (`id_treino`),
  CONSTRAINT `treinar_a_ibfk_1` FOREIGN KEY (`id_login`) REFERENCES `login` (`id`),
  CONSTRAINT `treinar_a_ibfk_2` FOREIGN KEY (`id_treino`) REFERENCES `treino_a` (`id_a`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `treinar_a`
--

LOCK TABLES `treinar_a` WRITE;
/*!40000 ALTER TABLE `treinar_a` DISABLE KEYS */;
INSERT INTO `treinar_a` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,8),(5,1,6),(6,1,7),(7,1,14),(8,2,2),(9,2,1),(10,2,8),(11,2,9),(12,2,13),(13,2,11),(14,3,4),(15,3,1),(16,3,2),(17,3,7),(18,3,6),(19,3,10),(20,4,5),(21,4,1),(22,4,3),(23,4,6),(24,4,7),(25,4,9),(26,4,10),(27,5,1),(28,5,5),(29,5,2),(30,5,6),(31,5,7);
/*!40000 ALTER TABLE `treinar_a` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `treinar_b`
--

DROP TABLE IF EXISTS `treinar_b`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `treinar_b` (
  `id_treina` int(11) NOT NULL AUTO_INCREMENT,
  `id_login` int(11) DEFAULT NULL,
  `id_treino` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_treina`),
  KEY `id_login` (`id_login`),
  KEY `id_treino` (`id_treino`),
  CONSTRAINT `treinar_b_ibfk_1` FOREIGN KEY (`id_login`) REFERENCES `login` (`id`),
  CONSTRAINT `treinar_b_ibfk_2` FOREIGN KEY (`id_treino`) REFERENCES `treino_b` (`id_b`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `treinar_b`
--

LOCK TABLES `treinar_b` WRITE;
/*!40000 ALTER TABLE `treinar_b` DISABLE KEYS */;
INSERT INTO `treinar_b` VALUES (1,1,5),(2,1,2),(3,1,1),(4,1,8),(5,1,4),(6,1,13),(7,1,12),(8,2,5),(9,2,2),(10,2,4),(11,2,8),(12,2,9),(13,3,2),(14,3,1),(15,3,4),(16,3,3),(17,3,5),(18,3,10),(19,4,2),(20,4,1),(21,4,3),(22,4,8),(23,4,11),(24,4,9),(25,5,5),(26,5,2),(27,5,6),(28,5,8),(29,5,13),(30,5,12);
/*!40000 ALTER TABLE `treinar_b` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `treinar_c`
--

DROP TABLE IF EXISTS `treinar_c`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `treinar_c` (
  `id_treina` int(11) NOT NULL AUTO_INCREMENT,
  `id_login` int(11) DEFAULT NULL,
  `id_treino` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_treina`),
  KEY `id_login` (`id_login`),
  KEY `id_treino` (`id_treino`),
  CONSTRAINT `treinar_c_ibfk_1` FOREIGN KEY (`id_login`) REFERENCES `login` (`id`),
  CONSTRAINT `treinar_c_ibfk_2` FOREIGN KEY (`id_treino`) REFERENCES `treino_c` (`id_c`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `treinar_c`
--

LOCK TABLES `treinar_c` WRITE;
/*!40000 ALTER TABLE `treinar_c` DISABLE KEYS */;
INSERT INTO `treinar_c` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,7),(5,1,8),(6,1,10),(7,1,9),(8,2,1),(9,2,2),(10,2,3),(11,2,6),(12,2,7),(13,3,3),(14,3,1),(15,3,2),(16,3,7),(17,3,6),(18,3,8),(19,4,3),(20,4,1),(21,4,2),(22,4,5),(23,4,7),(24,4,9),(25,4,8),(26,5,1),(27,5,2),(28,5,3),(29,5,7),(30,5,8),(31,5,10),(32,5,9);
/*!40000 ALTER TABLE `treinar_c` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `treino_a`
--

DROP TABLE IF EXISTS `treino_a`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `treino_a` (
  `id_a` int(11) NOT NULL AUTO_INCREMENT,
  `musculo` varchar(12) DEFAULT NULL,
  `exercício` varchar(30) DEFAULT NULL,
  `séries` tinyint(4) DEFAULT NULL,
  `repetições` int(11) DEFAULT NULL,
  `intervalo` time DEFAULT NULL,
  PRIMARY KEY (`id_a`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `treino_a`
--

LOCK TABLES `treino_a` WRITE;
/*!40000 ALTER TABLE `treino_a` DISABLE KEYS */;
INSERT INTO `treino_a` VALUES (1,'Peitoral','Supino reto',4,8,'00:01:30'),(2,'Peitoral','Supino inclinado',4,8,'00:01:30'),(3,'Peitoral','Cruxifixo reto',4,8,'00:01:30'),(4,'Peitoral','Crossover',4,8,'00:01:30'),(5,'Peitoral','Flexão de braço',4,8,'00:01:30'),(6,'Tríceps','Testa',4,8,'00:01:30'),(7,'Tríceps','Francês',4,8,'00:01:30'),(8,'Tríceps','Corda',4,8,'00:01:30'),(9,'Tríceps','No banco',4,8,'00:01:30'),(10,'Abdomen','Abdominal na polia',4,8,'00:01:30'),(11,'Abdomen','Abdominal remador',4,8,'00:01:30'),(12,'Abdomen','Abdominal infra',4,8,'00:01:30'),(13,'Abdomen','Prancha abdominal',4,8,'00:01:30'),(14,'Abdomen','Prancha lateral',4,8,'00:01:30');
/*!40000 ALTER TABLE `treino_a` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `treino_b`
--

DROP TABLE IF EXISTS `treino_b`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `treino_b` (
  `id_b` int(11) NOT NULL AUTO_INCREMENT,
  `musculo` varchar(12) DEFAULT NULL,
  `exercício` varchar(30) DEFAULT NULL,
  `séries` tinyint(4) DEFAULT NULL,
  `repetições` int(11) DEFAULT NULL,
  `intervalo` time DEFAULT NULL,
  PRIMARY KEY (`id_b`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `treino_b`
--

LOCK TABLES `treino_b` WRITE;
/*!40000 ALTER TABLE `treino_b` DISABLE KEYS */;
INSERT INTO `treino_b` VALUES (1,'Costas','Remada curvada supinada',4,8,'00:01:30'),(2,'Costas','Puxada aberta na frente',4,8,'00:01:30'),(3,'Costas','Remada unilateral',4,8,'00:01:30'),(4,'Costas','Pulldown',4,8,'00:01:30'),(5,'Costas','Barra fixa',4,8,'00:01:30'),(6,'Costas',' Remada curvada pronada',4,8,'00:01:30'),(7,'Costas','Pullover com halter',4,8,'00:01:30'),(8,'Costas','Remada cavalinho',4,8,'00:01:30'),(9,'Bíceps','Rosca direta',4,8,'00:01:30'),(10,'Bíceps','Rosca alternada com halteres',4,8,'00:01:30'),(11,'Bíceps','Rosca martelo',4,8,'00:01:30'),(12,'Bíceps','Rosca no banco Scott ',4,8,'00:01:30'),(13,'Bíceps','Rosca no banco inclinado ',4,8,'00:01:30');
/*!40000 ALTER TABLE `treino_b` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `treino_c`
--

DROP TABLE IF EXISTS `treino_c`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `treino_c` (
  `id_c` int(11) NOT NULL AUTO_INCREMENT,
  `musculo` varchar(30) NOT NULL,
  `exercício` varchar(40) NOT NULL,
  `séries` tinyint(4) NOT NULL,
  `repetições` int(11) NOT NULL,
  `intervalo` time NOT NULL,
  PRIMARY KEY (`id_c`)
) ENGINE=InnoDB AUTO_INCREMENT=121 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `treino_c`
--

LOCK TABLES `treino_c` WRITE;
/*!40000 ALTER TABLE `treino_c` DISABLE KEYS */;
INSERT INTO `treino_c` VALUES (1,'Quadríceps','Agachamento livre',4,8,'00:01:30'),(2,'Quadríceps','Leg press 45°',4,8,'00:01:30'),(3,'Quadríceps','Cadeira extensora',4,8,'00:01:30'),(4,'Quadríceps','Hacker',4,8,'00:01:30'),(5,'Quadríceps','Agachamento sumô ',4,8,'00:01:30'),(6,'Posterior de coxas','Stiff',4,8,'00:01:30'),(7,'Posterior de coxa','Mesa flexora',4,8,'00:01:30'),(8,'Deltoides','Elevação lateral',4,8,'00:01:30'),(9,'Deltoides','Desenvolvimento com halteres',4,8,'00:01:30'),(10,'Deltoides','Elevação frontal',4,8,'00:01:30');
/*!40000 ALTER TABLE `treino_c` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-08  9:48:38
