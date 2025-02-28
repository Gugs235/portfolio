create database atv_Mauricio_cadastro;
use atv_Mauricio_cadastro;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    telefone VARCHAR(15) NOT NULL,
    endereco VARCHAR(255) NOT NULL,
    data_nascimento DATE NOT NULL,
    sexo ENUM('Masculino', 'Feminino', 'Outro') NOT NULL,
    data_hora_cadastro datetime
);

drop database atv_Mauricio_cadastro;

select * from usuarios;
DESC usuarios;
ALTER TABLE usuarios ADD COLUMN foto VARCHAR(255);