create database Checkin_Cinema ;
use Checkin_Cinema;

CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY auto_increment,
    nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
);

CREATE TABLE cinemas (
    id INTEGER PRIMARY KEY auto_increment,
    nome TEXT NOT NULL,
    endereco TEXT NOT NULL
);

CREATE TABLE filmes (
    id INTEGER PRIMARY KEY auto_increment,
    titulo TEXT NOT NULL,
    duracao INTEGER NOT NULL, -- duração em minutos
    classificacao_etaria TEXT NOT NULL,
    data_lancamento DATE,
    genero TEXT,
    sinopse TEXT,
    trailer TEXT,  -- URL do trailer
    imagem TEXT    -- URL ou caminho da imagem do filme
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
    id INTEGER PRIMARY KEY auto_increment,
    id_usuario INTEGER NOT NULL,
    nome_cartao TEXT NOT NULL,
    numero_cartao TEXT NOT NULL,
    validade TEXT NOT NULL,
    cvv TEXT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios (id)
);

