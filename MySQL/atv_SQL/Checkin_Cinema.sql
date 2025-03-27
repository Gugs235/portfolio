create database Checkin_Cinema ;
use Checkin_Cinema;
SET SQL_SAFE_UPDATES = 0;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    sobrenome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL
);

CREATE TABLE cinemas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    endereco VARCHAR(255) NOT NULL
);

CREATE TABLE filmes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    cinema_id INT,
    duracao TIME NOT NULL,
    data_lancamento DATE NOT NULL,
    genero VARCHAR(255) NOT NULL,
    classificacao VARCHAR(255) NOT NULL,
    sinopse TEXT NOT NULL,
    trailer_url VARCHAR(255) NOT NULL,
    FOREIGN KEY (cinema_id) REFERENCES cinemas(id)
);

UPDATE filmes SET cinema_id = 1 WHERE cinema_id IS NULL;
UPDATE filmes SET data_lancamento = '2023-01-01' WHERE data_lancamento IS NULL;

CREATE TABLE salas (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_cinema INTEGER NOT NULL,
    numero INTEGER NOT NULL,
    capacidade INTEGER NOT NULL,
    tipo ENUM('convencional', 'IMAX', '3D', 'VIP', 'drive-in') NOT NULL DEFAULT 'convencional',
    FOREIGN KEY (id_cinema) REFERENCES cinemas (id)
);

CREATE TABLE sessoes (
    id INTEGER PRIMARY KEY auto_increment,
    id_filme INTEGER NOT NULL,
    id_sala INTEGER NOT NULL,
    data DATE NOT NULL,
    horario TIME NOT NULL,
    FOREIGN KEY (id_filme) REFERENCES filmes (id),
    FOREIGN KEY (id_sala) REFERENCES salas (id)
);

CREATE TABLE assentos (
    id INT NOT NULL AUTO_INCREMENT,
    id_sala INT NOT NULL,
    numero_assento VARCHAR(50) NOT NULL,
    status ENUM('livre', 'reservado') DEFAULT 'livre',
    PRIMARY KEY (id),
    FOREIGN KEY (id_sala) REFERENCES salas(id)
);

CREATE TABLE favoritos (
    id INTEGER PRIMARY KEY auto_increment,
    id_usuario INTEGER NOT NULL,
    id_filme INTEGER NOT NULL,
    data_favorito TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios (id),
    FOREIGN KEY (id_filme) REFERENCES filmes (id)
);

CREATE TABLE compras (
    id INTEGER PRIMARY KEY auto_increment,
    id_usuario INTEGER NOT NULL,
    id_sessao INTEGER NOT NULL,
    data_compra TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total REAL NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios (id),
    FOREIGN KEY (id_sessao) REFERENCES sessoes (id)
);

CREATE TABLE compras_assentos (
    id INTEGER PRIMARY KEY auto_increment,
    id_compra INTEGER NOT NULL,
    id_assento INTEGER NOT NULL,
    preco REAL NOT NULL,
    FOREIGN KEY (id_compra) REFERENCES compras (id),
    FOREIGN KEY (id_assento) REFERENCES assentos (id)
);

CREATE TABLE pagamentos (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    id_compra INTEGER NOT NULL,
    valor_total REAL NOT NULL,
    metodo ENUM('cartao_credito', 'cartao_debito', 'pix', 'boleto') NOT NULL,
    status ENUM('pendente', 'pago', 'cancelado') DEFAULT 'pendente',
    FOREIGN KEY (id_compra) REFERENCES compras (id)
);

CREATE TABLE cartoes (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    usuario_id INTEGER NOT NULL,
    nome_cartao TEXT NOT NULL,
    numero_cartao TEXT NOT NULL,
    data_expiracao TEXT NOT NULL,
    cvv TEXT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
);


CREATE TABLE IF NOT EXISTS usuarios (
	id INT AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(255) NOT NULL,
	sobrenome VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL UNIQUE,
	senha VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS cartoes (
	id INT AUTO_INCREMENT PRIMARY KEY,
	usuario_id INT,
	nome_cartao VARCHAR(255) NOT NULL,
	numero_cartao VARCHAR(16) NOT NULL,
	data_expiracao VARCHAR(5) NOT NULL,
	cvv VARCHAR(3) NOT NULL,
	FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE IF NOT EXISTS cinemas (
	id INT AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS filmes (
	id INT AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(255) NOT NULL,
	cinema_id INT,
	duracao TIME NOT NULL,
	data_lancamento DATE NOT NULL,
	genero VARCHAR(255) NOT NULL,
	classificacao VARCHAR(255) NOT NULL,
	sinopse TEXT NOT NULL,
	trailer_url VARCHAR(255) NOT NULL,
	poster_path VARCHAR(255),  -- Novo campo para o caminho do pôster
	FOREIGN KEY (cinema_id) REFERENCES cinemas(id)
);

CREATE TABLE IF NOT EXISTS sessoes (
	id INT AUTO_INCREMENT PRIMARY KEY,
	filme_id INT NOT NULL,
	cinema_id INT NOT NULL,
	data DATE NOT NULL,
	horario TIME NOT NULL,
	tipo_sala VARCHAR(255) NOT NULL,
	lotacao_maxima INT NOT NULL,
	FOREIGN KEY (filme_id) REFERENCES filmes(id),
	FOREIGN KEY (cinema_id) REFERENCES cinemas(id)
);

CREATE TABLE IF NOT EXISTS filmes (
	id INT AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(255) NOT NULL,
	cinema_id INT,
	duracao TIME NOT NULL,
	data_lancamento DATE NOT NULL,
	genero VARCHAR(255) NOT NULL,
	classificacao VARCHAR(255) NOT NULL,
	sinopse TEXT NOT NULL,
	trailer_url VARCHAR(255) NOT NULL,
	poster_data MEDIUMBLOB,  -- Novo campo para armazenar os dados binários da imagem
	FOREIGN KEY (cinema_id) REFERENCES cinemas(id)
);

CREATE TABLE IF NOT EXISTS assentos (
	id INT AUTO_INCREMENT PRIMARY KEY,
	sessao_id INT,
	numero VARCHAR(255) NOT NULL,
	reservado BOOLEAN NOT NULL DEFAULT FALSE,
	FOREIGN KEY (sessao_id) REFERENCES sessoes(id)
);

CREATE TABLE IF NOT EXISTS reservas (
	id INT AUTO_INCREMENT PRIMARY KEY,
	usuario_id INT,
	sessao_id INT,
	assento_id INT,
	forma_pagamento VARCHAR(255) NOT NULL,
	valor_total DECIMAL(10, 2) NOT NULL,
	FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
	FOREIGN KEY (sessao_id) REFERENCES sessoes(id),
	FOREIGN KEY (assento_id) REFERENCES assentos(id)
);

CREATE TABLE IF NOT EXISTS favoritos (
	id INT AUTO_INCREMENT PRIMARY KEY,
	usuario_id INT NOT NULL,
	filme_id INT NOT NULL,
	FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
	FOREIGN KEY (filme_id) REFERENCES filmes(id)
);


SET SQL_SAFE_UPDATES = 1;

#drop database Checkin_Cinema;

SELECT * FROM cartoes;

#SELECT * FROM filmes;
#SELECT * FROM favoritos;