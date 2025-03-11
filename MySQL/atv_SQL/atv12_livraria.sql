#1. Criação de um Banco de Dados de Livraria
#Objetivo: Criar um banco de dados para gerenciar livros e autores.

#Crie as tabelas livros (id, título, autor_id, preço) e autores (id, nome).

create database atv_livraria;
use atv_livraria;

create table autores (
id int primary key auto_increment not null,
nome varchar (50)

);

create table livros (
id int primary key auto_increment not null,
titulo varchar (50) not null,
autor_id int not null,
preco float not null,
foreign key (autor_id) references autores (id)
);


#Inserção: Adicione alguns livros e autores.
INSERT INTO autores (id, nome) VALUES
(1, 'Machado de Assis'),
(2, 'Clarice Lispector'),
(3, 'Graciliano Ramos'),
(4, 'José de Alencar'),
(5, 'Cecília Meireles'),
(6, 'Carlos Drummond de Andrade'),
(7, 'Monteiro Lobato'),
(8, 'Jorge Amado'),
(9, 'Ariano Suassuna'),
(10, 'Manuel Bandeira');

INSERT INTO livros (id, titulo, autor_id, preco) VALUES
(1, 'Dom Casmurro', 1, 39.90),
(2, 'Memórias Póstumas de Brás Cubas', 1, 42.50),
(3, 'A Hora da Estrela', 2, 35.00),
(4, 'Vidas Secas', 3, 45.90),
(5, 'O Guarani', 4, 30.00),
(6, 'Romanceiro da Inconfidência', 5, 29.50),
(7, 'A Rosa do Povo', 6, 38.00),
(8, 'O Sítio do Picapau Amarelo', 7, 44.90),
(9, 'Gabriela, Cravo e Canela', 8, 49.99),
(10, 'O Auto da Compadecida', 9, 37.75);


#Consulta: Liste todos os livros e seus autores.
SELECT livros.id, livros.titulo, autores.nome, livros.preco
FROM livros
INNER JOIN autores ON livros.autor_id = autores.id;

#Atualização: Atualize o preço de um livro específico.
update livros
set preco = 40.98
where id = 10;

#Exclusão: Exclua um autor e todos os livros associados a ele.
ALTER TABLE livros DROP FOREIGN KEY livros_ibfk_1; -- O nome pode variar, use `SHOW CREATE TABLE livros;` para verificar

ALTER TABLE livros 
ADD CONSTRAINT fk_livros_autor 
FOREIGN KEY (autor_id) REFERENCES autores(id) 
ON DELETE CASCADE;

DELETE FROM autores WHERE id = 5;  -- Substitua "1" pelo ID do autor que deseja excluir.
