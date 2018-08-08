CREATE DATABASE  IF NOT EXISTS `contaminantes2` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `contaminantes2`;
-- MySQL dump 10.13  Distrib 5.7.9, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: contaminantes2
-- ------------------------------------------------------
-- Server version	5.7.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `elementos`
--

DROP TABLE IF EXISTS `elementos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `elementos` (
  `id_elemento` int(11) NOT NULL AUTO_INCREMENT,
  `elemento` varchar(10) NOT NULL,
  `nombre_elemento` varchar(85) NOT NULL,
  `unidad_medicion` varchar(15) DEFAULT NULL,
  `significado_unidad` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_elemento`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elementos`
--

LOCK TABLES `elementos` WRITE;
/*!40000 ALTER TABLE `elementos` DISABLE KEYS */;
INSERT INTO `elementos` VALUES (1,'CO','MONÓXIDO DE CARBONO','PPM','PARTES POR MILLÓN'),(2,'NO2','DIÓXIDO DE NITRÓGENO','PPB','PARTES POR BILLÓN'),(3,'NOX','ÓXIDOS DE NITRÓGENO','PPB','PARTES POR BILLÓN'),(4,'O3','OZONO','PPB','PARTES POR BILLÓN'),(5,'SO2','DIÓXIDO DE AZUFRE','PPB','PARTES POR BILLÓN'),(6,'PM10','PARTÍCULAS MENORES A 10 MICRÓMETROS','UG/M3','MICROGRAMOS POR METRO CÚBICO'),(7,'NO','MONÓXIDO DE NITRÓGENO','PPB','PARTES POR BILLÓN'),(8,'PM25','PARTÍCULAS MENORES A 2.5 MICRÓMETROS','UG/M3','MICROGRAMOS POR METRO CÚBICO'),(9,'PMCO','PARTÍCULAS DE FRACCIÓN GRUESA','UG/M3','MICROGRAMOS POR METRO CÚBICO');
/*!40000 ALTER TABLE `elementos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estaciones`
--

DROP TABLE IF EXISTS `estaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `estaciones` (
  `id_estacion` int(11) NOT NULL AUTO_INCREMENT,
  `clave_estacion` varchar(10) NOT NULL,
  `nombre_estacion` varchar(35) NOT NULL,
  `delegacion_municipio` varchar(65) NOT NULL,
  `entidad` varchar(45) NOT NULL,
  `estatus` varchar(15) DEFAULT NULL,
  `domicilio` varchar(285) DEFAULT NULL,
  `latitud` double DEFAULT NULL,
  `longitud` double DEFAULT NULL,
  `altitud` varchar(15) DEFAULT NULL,
  `validado` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id_estacion`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estaciones`
--

LOCK TABLES `estaciones` WRITE;
/*!40000 ALTER TABLE `estaciones` DISABLE KEYS */;
INSERT INTO `estaciones` VALUES (1,'ACO','Acolman','Acolman','Estado de México','ACTIVA','Calzada de los Agustinos s/n, Col. Centro, C.P. 55870',19.635501,-98.912003,'2198 msnm',1),(2,'AJU','Ajusco','Tlalpan','CDMX','ACTIVA','Km 36.5 Carretera Federal México-Cuernavaca, C.P. 14500',19.154674,-99.162459,'2953 msnm',1),(3,'AJM','Ajusco Medio','Tlalpan','CDMX','ACTIVA','Encinos # 41, col. Miguel Hidalgo 4ta sección, Tlalpan, C.P. 14250',19.2721,-99.207658,'2619 msnm',1),(4,'ATI','Atizapán','Atizapán de Zaragoza','Estado de México','ACTIVA','Oceano Pacífico s/n, Col. Lomas Lindas, C.P. 54947',19.576963,-99.254133,'2341 msnm',1),(5,'BJU','Benito Juarez','Benito Juárez','CDMX','ACTIVA','Municipio libre y Uxmal, Col. Santa Cruz Atoyac,Benito Juárez,C.P.03310',19.371612,-99.158969,'2250 msnm',1),(6,'CAM','Camarones','Azcapotzalco','CDMX','ACTIVA','Malvón No. 20, Col. Hogar y seguridad, C.P. 02820',19.468404,-99.169794,'2233 msnm',1),(7,'CCA','Centro de Ciencias de la Atmósfera','Coyoacán','CDMX','ACTIVA','Universidad Nacional Autónoma de México, Circuito Exterior s/n, Ciudad Universitaria, Coyoacán, C.P. 04510',19.3262,-99.1761,'2280 msnm',1),(8,'TEC','Cerro del Tepeyac','Gustavo A. Madero','CDMX','ACTIVA','Av. Hidalgo y Av. Cantera s/n, Col. Estansuela, C.P. 07060',19.487227,-99.114229,'2265 msnm',1),(9,'CHO','Chalco','Chalco','Estado de México','ACTIVA','Insurgentes s/n, Col. Casco de San Juan, C.P. 56600',19.266948,-98.886088,'2253 msnm',1),(10,'COR','CORENA','Xochimilco','CDMX','ACTIVA','Av. Año de Juárez N° 9700, Col. Quirino Mendoza, Pueblo de San Luis Tlaxialtemalco, C.P. 16610',19.265346,-99.02604,'2242 msnm',1),(11,'COY','Coyoacán','Coyoacán','CDMX','ACTIVA','Av. Hidalgo No. 62, Col. Del Carmen Coyoacán, C.P. 04000',19.350258,-99.157101,'2260 msnm',1),(12,'CUA','Cuajimalpa','Cuajimalpa de Morelos','CDMX','ACTIVA','Monte Encino No. 14, Col. Jesús del Monte, C.P. 05260',19.365313,-99.291705,'2704 msnm',1),(13,'CUT','Cuautitlán','Tepotzotlán','Estado de México','ACTIVA','Carretera Circunvalación s/n, Col. El Trebol, C.P. 54600',19.722186,-99.198602,'2263 msnm',1),(14,'DIC','Diconsa','Tlalpan','CDMX','ACTIVA','Insurgentes Sur No. 3483, Col. Villa Olimpica Miguel Hidalgo, C.P. 14020',19.298819,-99.185774,'2305 msnm',1),(15,'EAJ','Ecoguardas Ajusco','Tlalpan','CDMX','ACTIVA','Carretera Picacho-Ajusco km. 5.5, Col. Ampliación Miguel Hidalgo, C.P. 14250',19.271222,-99.203971,'2584 msnm',1),(16,'EDL','Ex Convento Desierto de los Leones','Cuajimalpa de Morelos','CDMX','ACTIVA','Camino al Desierto de los Leones s/n, Col. La Venta, C.P. 05520',19.313357,-99.310635,'2980 msnm',1),(17,'FAC','FES Acatlán','Naucalpan de Juárez','Estado de México','ACTIVA','Av. Alcanfores y San Juan Totoltepec s/n, Col. Santa Cruz Acatlán, C.P. 53150',19.482473,-99.243524,'2299 msnm',1),(18,'GAM','Gustavo A. Madero','Gustavo A. Madero','CDMX','ACTIVA','Av. Ing. Eduardo Molina No. 1577, Col. Salvador Diaz Miron, C.P. 07400',19.4827,-99.094517,'2227 msnm',1),(19,'HGM','Hospital General de México','Cuauhtémoc','CDMX','ACTIVA','Calle Sur 128 No. 53, Col. América, Miguel Hidalgo, C.P. 11820',19.40405,-99.202603,'2366 msnm',1),(20,'INN','Investigaciones Nucleares','Ocoyoacac','Estado de México','ACTIVA','Carretera México-Toluca s/n, La Marquesa, Ocoyoacac, C.P. 52750',19.291968,-99.38052,'3082 msnm',1),(21,'IZT','Iztacalco','Iztacalco','CDMX','ACTIVA','Guillermo Prieto y Melchor Ocampo No. 73, Col. Campamento 2 de octubre, C.P. 08930',19.384413,-99.117641,'2238 msnm',1),(22,'LPR','La Presa','Tlalnepantla de Baz','Estado de México','ACTIVA','Asociación Mexicana de Excursionistas del D.F. s/n, Col. La Presa, C.P. 54189',19.534727,-99.11772,'2302 msnm',1),(23,'LAA','Laboratorio de Análisis Ambiental','Gustavo A. Madero','CDMX','ACTIVA','Av. Sur de los Cien Metros s/n, Col. Nueva Vallejo, C.P. 07750',19.483781,-99.147312,'2255 msnm',1),(24,'IBM','Legaria','Miguel Hidalgo','CDMX','ACTIVA','Calz. Legaria No. 853, Col. Irrigación, C.P. 11500',19.443319,-99.21536,'2314 msnm',1),(25,'LOM','Lomas','Miguel Hidalgo','CDMX','ACTIVA','Ciruelo No. 99, Col. Bosques de las Lomas, C.P. 11700',19.403,-99.242062,'2434 msnm',1),(26,'LLA','Los Laureles','Ecatepec de Morelos','Estado de México','ACTIVA','Río Piedad esq. Ponce s/n, Col. Fracc. Río Piedras, C.P. 55090',19.578792,-99.039644,'2230 msnm',1),(27,'MER','Merced','Venustiano Carranza','CDMX','ACTIVA','Congreso de la Unión esq. Stan de Tiro s/n, Col. Merced Balbuena, C.P. 15860',19.42461,-99.119594,'2245 msnm',1),(28,'MGH','Miguel Hidalgo','Miguel Hidalgo','CDMX','ACTIVA','Calle Sur 128 No. 53, Col. América, Miguel Hidalgo, C.P. 11820',19.40405,-99.202603,'2366 msnm',1),(29,'MPA','Milpa Alta','Milpa Alta','CDMX','ACTIVA','Blvd. Nuevo León No. 386, Col. Villa Milpa Alta, C.P. 12000',19.1769,-98.990189,'2594 msnm',1),(30,'MON','Montecillo','Texcoco','Estado de México','ACTIVA','Km. 36,5 carretera México - Texcoco, Col. Montecillo, C.P. 56230',19.460415,-98.902853,'2252 msnm',1),(31,'MCM','Museo de la Ciudad de México','Cuauhtémoc','CDMX','ACTIVA','Pino Suárez No. 30, Col. Centro, C.P. 06000',19.429071,-99.131924,'2237 msnm',1),(32,'NEZ','Nezahualcóyotl','Nezahualcóyotl','Estado de México','ACTIVA','Av. Ángel de la Independencia s/n, Col. Metropolitana 2a sección, C.P. 57740',19.393734,-99.028212,'2235 msnm',1),(33,'PED','Pedregal','Álvaro Obregón','CDMX','ACTIVA','Cañada No. 370, Col. Jardines del Pedregal, C.P. 01900',19.325146,-99.204136,'2326 msnm',1),(34,'SAG','San Agustín','Ecatepec de Morelos','Estado de México','ACTIVA','Av. Santa Rita y Sur 92, Col. San Agustín 3a sección, C.P. 55130',19.532968,-99.030324,'2241 msnm',1),(35,'SJA','San Juan de Aragón','Gustavo A. Madero','CDMX','ACTIVA','Av. 504 y 506 s/n 2a sección, Col. Unidad San Juan de Aragón, C.P. 07920',19.452592,-99.086095,'2258 msnm',1),(36,'SNT','San Nicolás Totolapan','La Magdalena Contreras','CDMX','ACTIVA','Km. 11.5 carretera Picacho-Ajusco, C.P. 10900',19.250385,-99.256462,'2946 msnm',1),(37,'SFE','Santa Fe','Cuajimalpa de Morelos','CDMX','ACTIVA','Av. Carlos Lazo s/n, entre Tamaulipas y Sta. Fe, Col. Prados de la Montaña, C.P. 05619',19.357357,-99.262865,'2599 msnm',1),(38,'SHA','Secretaría de Hacienda','Miguel Hidalgo','CDMX','ACTIVA','Calz. Legaria No. 608, Col. Irrigación, C.P. 11500',19.446203,-99.207868,'2272 msnm',1),(39,'TAH','Tláhuac','Xochimilco','CDMX','ACTIVA','Escudo Nacional s/n, Col Nativitas, C.P. 16790',19.246459,-99.010564,'2297 msnm',1),(40,'TLA','Tlalnepantla','Tlalnepantla de Baz','Estado de México','ACTIVA','Glorieta Atlacomulco s/n, Col. Tlalnemex, C.P. 54070',19.529077,-99.204597,'2311 msnm',1),(41,'TLI','Tultitlán','Tultitlán','Estado de México','ACTIVA','Blvd. Lomas de Cartagena s/n, Col. Lomas de Cartagena, C.P. 54943',19.602542,-99.177173,'2313 msnm',1),(42,'UIZ','UAM Iztapalapa','Iztapalapa','CDMX','ACTIVA','San Rafael Atlixco No. 180, Col. Vicentina, C.P. 09340',19.360794,-99.07388,'2221 msnm',1),(43,'UAX','UAM Xochimilco','Coyoacán','CDMX','ACTIVA','Calz.del Hueso 1100, Col. Villa Quietud, C.P. 04960',19.304441,-99.103629,'2246 msnm',1),(44,'VIF','Villa de las Flores','Coacalco de Berriozábal','Estado de México','ACTIVA','Primavera y Palmacristi s/n, Col. Villa de las Flores, C.P. 55710',19.658223,-99.09659,'2242 msnm',1),(45,'XAL','Xalostoc','Ecatepec de Morelos','Estado de México','ACTIVA','Vía Morelos km 12.5, Col. Xalostoc, entre López Rayón y Av. Benito Juárez, C.P. 54190',19.525995,-99.0824,'2160 msnm',1),(46,'LAG','Lagunilla','Cuauhtémoc','CDMX','INACTIVA','Republica del Ecuador, esquina caclle Comonfort',19.44242,-99.135183,'2223 msnm',1),(47,'CES','Cerro de la Estrella','Iztapalapa','CDMX','INACTIVA','Av. San Lorenzo',19.334731,-99.074678,'2219 msnm',1),(48,'ARA','Aragón','Gustavo A. Madero','CDMX','INACTIVA','Av. 485',19.470218,-99.074549,'2200 msnm',1),(49,'IMP','Inst. Mexicano del Petróleo','Gustavo A. Madero','CDMX','INACTIVA','Calle Pte. 128',19.487561,-99.147294,'2250 msnm',1),(50,'TAX','Taxqueña','Coyoacán','CDMX','INACTIVA','Av. H. Escuela Naval Militar',19.335689,-99.123204,'2242 msnm',1),(51,'CUI','Cuitláhuac','Miguel Hidalgo','CDMX','INACTIVA','Calle Narciso',19.469859,-99.165849,'2255 msnm',1),(52,'AZC','Azcapotzalco','Azcapotzalco','CDMX','INACTIVA','Calle Chamulas',19.487728,-99.198657,'2279 msnm',1),(53,'PLA','Plateros','Cuauhtémoc','CDMX','INACTIVA','Calle Azcapotzalco, Col. Los plateros',19.365869,-99.200109,'2345 msnm',1),(54,'HAN','Hangares','Venustiano Carranza','CDMX','INACTIVA','Calle Sección 9',19.420518,-99.083623,'2235 msnm',1),(55,'SUR','Santa Ursula','Coyoacán','CDMX','INACTIVA','Calle San Gabriel',19.31448,-99.149994,'2279 msnm',1),(56,'TAC','Tacuba','Miguel Hidalgo','CDMX','INACTIVA','Calle Ignacio Allende',19.453907,-99.202455,'2275 msnm',1),(57,'LVI','La Villa','Gustavo A. Madero','CDMX','INACTIVA','Av. Sara',19.46789,-99.117749,'2228 msnm',1),(58,'NET','Netzahualcoyotl','Nezahualcóyotl','Estado de México','INACTIVA','Calle Clavel esquina con Lirio',19.42115,-99.026119,'2230 msnm',1),(59,'MIN','Metro Insurgentes','Cuauhtémoc','CDMX','INACTIVA','Calle Pomona',19.42144,-99.162885,'2231 msnm',1),(60,'VAL','Vallejo','Gustavo A. Madero','CDMX','INACTIVA','Calz. Vallejo',19.522437,-99.165702,'2248 msnm',1),(61,'TPN','Tlalpan','Tlalpan','CDMX','INACTIVA','Calle Tlalmille',19.257041,-99.184177,'2522 msnm',1),(62,'PER','La Perla','Netzahualcoyotl','Estado de México','INACTIVA','Calle Pte. 23',19.38286,-98.991858,'2237 msnm',1);
/*!40000 ALTER TABLE `estaciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mediciones`
--

DROP TABLE IF EXISTS `mediciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mediciones` (
  `id_medicion` int(11) NOT NULL AUTO_INCREMENT,
  `id_estacion` int(11) DEFAULT NULL,
  `id_elemento` int(11) DEFAULT NULL,
  `medicion` double DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `hora` int(11) NOT NULL,
  PRIMARY KEY (`id_medicion`),
  KEY `ref_estacion_idx` (`id_estacion`),
  KEY `ref_elemento_idx` (`id_elemento`)
) ENGINE=InnoDB AUTO_INCREMENT=36199774 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mediciones`
--

LOCK TABLES `mediciones` WRITE;
/*!40000 ALTER TABLE `mediciones` DISABLE KEYS */;
/*!40000 ALTER TABLE `mediciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'contaminantes2'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-07-16 13:43:40
