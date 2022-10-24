create TABLE if NOT EXISTS cita(
	id_especialista INT(11) NOT NULL,
	username INT(11) NOT NULL,
	fecha DATETIME NOT NULL,
	PRIMARY KEY (id_especialista, username,fecha) USING BTREE,
	KEY FK_usuario (username), 
	CONSTRAINT FK_especialista FOREIGN KEY (id_especialista) REFERENCES especialista (id_especialista),
	CONSTRAINT FK_usuario FOREIGN KEY (username) REFERENCES usuario (username)
)ENGINE=INNODB DEFAULT CHARSET=LATIN1;