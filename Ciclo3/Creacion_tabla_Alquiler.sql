create TABLE if NOT EXISTS alquiler(
	id INT(11) NOT NULL,
	username VARCHAR(100) NOT NULL,
	fecha DATETIME NOT NULL,
	PRIMARY KEY (id, username,fecha) USING BTREE,
	KEY FK_usuario (username), 
	CONSTRAINT FK_pelicula FOREIGN KEY (id) REFERENCES pelicula (id),
	CONSTRAINT FK_usuario FOREIGN KEY (username) REFERENCES usuario (username)
)ENGINE=INNODB DEFAULT CHARSET=LATIN1;