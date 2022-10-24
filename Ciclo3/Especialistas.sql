USE aces;
CREATE TABLE IF NOT EXISTS especialista(
	id_especialista INT(11) NOT NULL,
	pass__especialista VARCHAR(100) NOT NULL, 
	nombre_especialista VARCHAR(100) DEFAULT NULL,
	apellido_especialista VARCHAR(100) DEFAULT NULL,
	tipo_especialista VARCHAR(100) DEFAULT NULL,
	email_especialista VARCHAR(100) DEFAULT NULL,
	PRIMARY KEY (id_especialista)
) ENGINE=INNODB DEFAULT CHARSET=LATIN1;
CREATE TABLE if NOT EXISTS cita(
	id_especialista INT(11) NOT NULL,
	username VARCHAR(100) NOT NULL,
	fecha DATETIME NOT NULL,
	PRIMARY KEY (id_especialista, username,fecha) USING BTREE,
	KEY FK_usuario (username), 
	CONSTRAINT FK_especialista FOREIGN KEY (id_especialista) REFERENCES especialista (id_especialista),
	CONSTRAINT FK_usuario FOREIGN KEY (username) REFERENCES usuario (username)
)ENGINE=INNODB DEFAULT CHARSET=LATIN1;

