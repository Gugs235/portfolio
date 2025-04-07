create database Checkin_Cinema ;
use Checkin_Cinema;
SET SQL_SAFE_UPDATES = 0;

CREATE TABLE cinemas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    endereco VARCHAR(255) NOT NULL
);

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    sobrenome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL
);

CREATE TABLE tipos_ingresso (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    desconto_percentual DECIMAL(5,2) NOT NULL DEFAULT 0.00
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

CREATE TABLE salas (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_cinema INTEGER NOT NULL,
    numero INTEGER NOT NULL,
    capacidade INTEGER NOT NULL,
    tipo ENUM('convencional', 'IMAX', '3D', 'VIP', 'drive-in') NOT NULL DEFAULT 'convencional',
    FOREIGN KEY (id_cinema) REFERENCES cinemas (id)
);

CREATE TABLE sessoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_filme INT NOT NULL,
    id_sala INTEGER NOT NULL,
    data DATE NOT NULL,
    horario TIME NOT NULL,
    sala VARCHAR(10) NOT NULL,
    preco DECIMAL(10,2) NOT NULL DEFAULT 20.00,
    id_cinema int,
    FOREIGN KEY (id_filme) REFERENCES filmes(id),
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

CREATE TABLE reservas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_sessao INT NOT NULL,
    id_assento INT NOT NULL,
    id_tipo_ingresso INT,
    forma_pagamento VARCHAR(50) NOT NULL,
    valor_total DECIMAL(10,2) NOT NULL,
    data_reserva TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    FOREIGN KEY (id_sessao) REFERENCES sessoes(id),
    FOREIGN KEY (id_assento) REFERENCES assentos(id),
    FOREIGN KEY (id_tipo_ingresso) REFERENCES tipos_ingresso(id)
);

CREATE TABLE favoritos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_filme INT NOT NULL,
    UNIQUE KEY unique_favorito (id_usuario, id_filme),  -- Garante que não haja duplicatas
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    FOREIGN KEY (id_filme) REFERENCES filmes(id)
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
    FOREIGN KEY (id_compra) REFERENCES compras(id),
    FOREIGN KEY (id_assento) REFERENCES assentos(id)
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
    data_expiracao TEXT NOT NULL,  -- Alterado de 'validade' para 'data_expiracao'
    cvv TEXT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- Inserir tipos de ingresso
INSERT INTO tipos_ingresso (nome, desconto_percentual) VALUES 
('Inteira', 0.00),
('Meia-Entrada', 50.00),
('Idoso', 50.00),
('Estudante', 50.00),
('Professor', 30.00),
('PCD', 50.00) -- Pessoa com Deficiência, exemplo de tipo especial
ON DUPLICATE KEY UPDATE desconto_percentual = VALUES(desconto_percentual);
    
    
-- Atualizações (após inserções para evitar afetar linhas inexistentes)
UPDATE filmes SET cinema_id = 1 WHERE cinema_id IS NULL;
UPDATE filmes SET data_lancamento = '2023-01-01' WHERE data_lancamento IS NULL;
UPDATE sessoes SET preco = 20.00 WHERE preco IS NULL;

-- Alteração na tabela reservas (após criação inicial)
ALTER TABLE reservas
ADD COLUMN tipo_ingresso_id INT,
ADD CONSTRAINT fk_tipo_ingresso FOREIGN KEY (tipo_ingresso_id) REFERENCES tipos_ingresso(id);

SELECT * FROM usuarios;
SELECT * FROM filmes;
SELECT * FROM favoritos;

DESCRIBE cartoes;
DESCRIBE sessoes;


SET SQL_SAFE_UPDATES = 1;
#drop database Checkin_Cinema;