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

-- Volcando estructura para tabla aces.cita
CREATE TABLE IF NOT EXISTS `cita` (
  `id_especialista` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `novedad` tinyint(4) DEFAULT NULL,
  `genero` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_especialista`,`username`,`fecha`) USING BTREE,
  KEY `FK_usuario` (`username`),
  CONSTRAINT `FK_especialista` FOREIGN KEY (`id_especialista`) REFERENCES `especialista` (`id_especialista`),
  CONSTRAINT `FK_usuario` FOREIGN KEY (`username`) REFERENCES `usuario` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla aces.cita: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `cita` DISABLE KEYS */;
/*!40000 ALTER TABLE `cita` ENABLE KEYS */;

-- Volcando estructura para tabla aces.especialista
CREATE TABLE IF NOT EXISTS `especialista` (
  `id_especialista` int(11) NOT NULL,
  `pass_especialista` varchar(100) NOT NULL,
  `nombre_especialista` varchar(100) DEFAULT NULL,
  `apellido_especialista` varchar(100) DEFAULT NULL,
  `tipo_especialista` varchar(100) DEFAULT NULL,
  `email_especialista` varchar(100) DEFAULT NULL,
  `novedad` tinyint(4) DEFAULT NULL,
  `citas_especialista` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id_especialista`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla aces.especialista: ~10 rows (aproximadamente)
/*!40000 ALTER TABLE `especialista` DISABLE KEYS */;
INSERT INTO `especialista` (`id_especialista`, `pass_especialista`, `nombre_especialista`, `apellido_especialista`, `tipo_especialista`, `email_especialista`, `novedad`, `citas_especialista`) VALUES
	(2122, 'Interestelar4324', 'Aldemar', 'Moncaleano  Vasquez', 'Cardiologo', 'aldemarmoncaleanovasquez76878@hotmail.com', NULL, NULL),
	(2345, 'The shape of water 4224', 'Alejandra', 'Ramirez Sanchez', 'Oftamologo', 'alejaramirezsan2312@hotmail.com', NULL, NULL),
	(3451, 'Hellraiser8769678', 'Jennifer', 'Gomez Tula', 'Odontologo', 'jennifergomeztula455645@hotmail.com', NULL, NULL),
	(4354, 'el conjuro2544', 'Esperanza', 'Sanchez Castillo', 'Ginecologo', 'esperasanchezcas54345@hotmail.com', NULL, NULL),
	(4543, 'el laberinto del fauno245', 'Nicolas', 'Arregoces Sanchez', 'Cardiologo', 'nicolasarregocessan23123@hotmail.com', NULL, NULL),
	(4565, 'desde mi cielo3242', 'Laura', 'Salazar Perdomo', 'Otorrinolaringologo', 'laurasalazarperdomo35432@hotmail.com', NULL, NULL),
	(5675, 'white chick768s', 'Maria Fernanda', 'Tovar Valenzuela', 'Ginecologo', 'mariafernanda323tovar6565@hotmail.com', NULL, NULL),
	(6756, 'Man of stell389', 'German Andres', 'Ramirez Piña', 'Oftamologo', 'germanremiresandres21231@hotmail.com', NULL, NULL),
	(8767, 'La sirenita83', 'Michael Andres', 'Galeano', 'Ginecologo', 'michaelandresgaleano12235@hotmail.com', NULL, NULL),
	(9877, 'Thorsefdf435', 'Helena', 'Salazar', 'Urologo', 'helenasalazar5443@hotmail.com', NULL, NULL);
/*!40000 ALTER TABLE `especialista` ENABLE KEYS */;

-- Volcando estructura para tabla aces.usuario
CREATE TABLE IF NOT EXISTS `usuario` (
  `username` varchar(100) NOT NULL,
  `pass` varchar(100) NOT NULL,
  `nombre_usuario` varchar(100) DEFAULT NULL,
  `apellido_usuario` varchar(100) DEFAULT NULL,
  `email_usuario` varchar(100) DEFAULT NULL,
  `eps_usuario` varchar(100) DEFAULT NULL,
  `citas_usuario` int(15) DEFAULT NULL,
  `premium` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla aces.usuario: ~16 rows (aproximadamente)
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` (`username`, `pass`, `nombre_usuario`, `apellido_usuario`, `email_usuario`, `eps_usuario`, `citas_usuario`, `premium`) VALUES
	('10547861', 'The shape of water 4224', ' Maria Alejandra', 'Ramos Sanchez', 'alejaramirezsan2312@hotmail.com', 'Nueva EPS', NULL, NULL),
	('1234', '1234', 'admin', 'admin', 'admin@gmail.com', 'Nueva Eps', 2, 1),
	('16161530', 'visto en el hospital 3212', 'Wilson', 'Cortes García', 'wilsoncortesgarcía@gmail.com', 'Sanitas', NULL, NULL),
	('19486530', 'e remite para valoración32132', 'Andrés Iván ', 'Yépez', 'andrésiványépez32321@gmail.com', 'Sanitas', NULL, NULL),
	('2071579475', 'Hiperpigmentación de la cara', ' Yenffer Alonso ', 'Mahecha Alarcón', 'yenfferalonsomahechaalarcón@gmail.com', 'Famisanar', NULL, NULL),
	('25137486', 'ANTECEDENTES: Vacuna COVID', ' Hermelina', 'Rodríguez de Bernal', 'hermelinarodríguezdeberna@gmail.com', 'Compensar', NULL, NULL),
	('254553065', 'Tobrex gotas aplicar cada 3 horas', 'Daniela ', 'Castro Dussan', ' danielacastrodussan@hotmail.com', 'Salud Total', NULL, NULL),
	('3504425', 'KERATOMETRIA umefacción 33', 'Angela Lizeth', 'Castro Correa', 'angelalizethcastrocorrea@hotmail.com', 'Medimas', NULL, NULL),
	('4439443', 'dos policías 321 golpearon la cara', 'Jhornan Andrés', 'González Pardo', 'jhornanandrésgonzálezpardo@hotmail.com', 'Colsubsidio', NULL, NULL),
	('6455645645', 'saasdfs AKQ 123Qx@q', 'Laura Natalia', 'Velez Camacho', 'lauranataliavelez233@gmail.com', 'Salud Total', NULL, NULL),
	('8527992', ' artificiales y Tobramicina +', 'Susana', ' De la Cruz', 'susanadelacruz324@gmail.com', 'Nueva EPS', NULL, NULL),
	('admin', 'admin', 'Nicolas', 'Arregoces', 'campniko56@gmail.com', NULL, NULL, NULL),
	('adminfbfd', '123', 'Nicolas', 'Developer', 'campnik@gmail.com', NULL, NULL, NULL),
	('bbbb', '1234', 'Nicolas', 'Arregoces', 'campniko56@gmail.com', NULL, NULL, NULL),
	('dfgdssds', 'dfdf', 'Nicolas', 'Arregoces', 'campniko56@gmail.com', NULL, NULL, NULL),
	('sadasdasd', '1234', 'Nicolas', 'Arregoces', 'campniko56@gmail.com', NULL, NULL, NULL);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
