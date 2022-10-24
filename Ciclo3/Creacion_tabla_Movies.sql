Use movies_rental;
CREATE TABLE IF NOT EXISTS usuario(
	username VARCHAR(100) NOT NULL,
	contrasena VARCHAR(100) NOT NULL, 
	nombre VARCHAR(100) DEFAULT NULL,
	apellido VARCHAR(100) DEFAULT NULL,
	email VARCHAR(100) DEFAULT NULL,
	saldo DOUBLE(22,2) DEFAULT NULL,
	premium TINYINT(4) DEFAULT NULL,
	PRIMARY KEY (username)
) ENGINE=INNODB DEFAULT CHARSET=LATIN1;

CREATE TABLE IF NOT EXISTS pelicula (
 	id INT(11) NOT NULL,
 	titulo VARCHAR(100) DEFAULT NULL,
 	genero VARCHAR(100) DEFAULT NULL,
 	autor VARCHAR(100) DEFAULT NULL,
 	copias INT(11) DEFAULT NULL,
 	novedad TINYINT(4) DEFAULT NULL,
 	PRIMARY KEY (id)
) ENGINE=INNODB DEFAULT CHARSET=LATIN1;