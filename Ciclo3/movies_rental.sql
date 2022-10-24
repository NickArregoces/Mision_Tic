-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.9.2-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para movies_rental
CREATE DATABASE IF NOT EXISTS `movies_rental` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `movies_rental`;

-- Volcando estructura para tabla movies_rental.alquiler
CREATE TABLE IF NOT EXISTS `alquiler` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `fecha` datetime NOT NULL,
  PRIMARY KEY (`id`,`username`,`fecha`) USING BTREE,
  KEY `FK_usuario` (`username`),
  CONSTRAINT `FK_pelicula` FOREIGN KEY (`id`) REFERENCES `pelicula` (`id`),
  CONSTRAINT `FK_usuario` FOREIGN KEY (`username`) REFERENCES `usuario` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla movies_rental.alquiler: ~21 rows (aproximadamente)
/*!40000 ALTER TABLE `alquiler` DISABLE KEYS */;
INSERT INTO `alquiler` (`id`, `username`, `fecha`) VALUES
	(1, '1234', '2022-09-27 09:22:54'),
	(1, '1234', '2022-09-27 09:23:19'),
	(1, '1234', '2022-09-27 10:09:36'),
	(1, '1234', '2022-09-27 10:09:39'),
	(1, '1234', '2022-09-27 10:14:27'),
	(2, '1234', '2022-09-27 09:23:22'),
	(2, '1234', '2022-09-27 10:17:37'),
	(2, '1234', '2022-09-27 10:24:36'),
	(2, '1234', '2022-09-27 10:24:39'),
	(2, '1234', '2022-09-27 10:32:33'),
	(2, '1234', '2022-09-27 10:37:22'),
	(3, '1234', '2022-09-27 10:32:30'),
	(3, '1234', '2022-09-27 10:40:02'),
	(3, '1234', '2022-09-27 10:42:21'),
	(4, '1234', '2022-09-27 10:38:08'),
	(7, '1234', '2022-09-27 09:22:38'),
	(7, '1234', '2022-09-27 09:22:44'),
	(8, '1234', '2022-09-27 09:22:48'),
	(8, '1234', '2022-09-27 09:22:51'),
	(8, '1234', '2022-09-27 09:46:09'),
	(10, '1234', '2022-09-27 09:22:57'),
	(10, '1234', '2022-09-27 09:46:14');
/*!40000 ALTER TABLE `alquiler` ENABLE KEYS */;

-- Volcando estructura para tabla movies_rental.pelicula
CREATE TABLE IF NOT EXISTS `pelicula` (
  `id` int(11) NOT NULL,
  `titulo` varchar(100) DEFAULT NULL,
  `genero` varchar(100) DEFAULT NULL,
  `autor` varchar(100) DEFAULT NULL,
  `copias` int(11) DEFAULT NULL,
  `novedad` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla movies_rental.pelicula: ~10 rows (aproximadamente)
/*!40000 ALTER TABLE `pelicula` DISABLE KEYS */;
INSERT INTO `pelicula` (`id`, `titulo`, `genero`, `autor`, `copias`, `novedad`) VALUES
	(1, 'The shape of water', '/Fantasia', 'Guillermo del toro', 0, 0),
	(2, 'el laberinto del fauno', 'Fantasia/Belico', 'Guillermo del toro', 0, 1),
	(3, 'el conjuro', 'terror/documental', 'James Wan', 0, 0),
	(4, 'Man of stell', 'DC/Superheroes', 'Zack Snyder', 9, 0),
	(5, 'La sirenita', 'Infantil/Animacion', 'Disney', 10, 0),
	(6, 'Thor', 'Marvel/Superheroes', 'Disney', 8, 1),
	(7, 'Interestelar', 'Accion/Ciencia Ficcion', 'Christopher nolan', 4, 1),
	(8, 'desde mi cielo', 'Drama/Suspenso', 'piter Jackson', 4, 0),
	(9, 'white chicks', 'Comedia/familiar', 'wattsons', 8, 1),
	(10, 'Hellraiser', 'Terror/Suspenso', 'Anthony hickox', 5, 0);
/*!40000 ALTER TABLE `pelicula` ENABLE KEYS */;

-- Volcando estructura para tabla movies_rental.usuario
CREATE TABLE IF NOT EXISTS `usuario` (
  `username` varchar(100) NOT NULL,
  `contrasena` varchar(100) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `apellidos` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `saldo` double(22,2) DEFAULT NULL,
  `premium` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla movies_rental.usuario: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` (`username`, `contrasena`, `nombre`, `apellidos`, `email`, `saldo`, `premium`) VALUES
	('1234', '1234', 'admin', 'admin', 'admin@hotmail.com', 189.20, 1),
	('admindsds', 'admin', 'Nicolas', 'arrefggf', 'fdggdfgff@gmail', 5.00, 1),
	('adminfggfg', 'admin', 'Nicolas', 'Arregoces', 'campniko56@gmail.com', 4.00, 0),
	('fdgfdfdg', '1234', 'Nicolas', 'Arregoces', 'campniko56@gmail.com', 1223.00, 0);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
