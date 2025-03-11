#4. Sistema de Controle de Estoque
#Objetivo: Criar um banco de dados para controlar o estoque de produtos.

create database atv15_ControleEstoque;
use atv15_ControleEstoque;

#Crie as tabelas produtos (id, nome, quantidade, preco).
CREATE TABLE produtos (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nome VARCHAR(50) NOT NULL,
    quantidade INT NOT NULL,
    preco FLOAT NOT NULL
);

#Inserção: Adicione produtos ao estoque.
INSERT INTO produtos (nome, quantidade, preco) VALUES
('Arroz', 100, 25.50),
('Feijão', 150, 10.30),
('Macarrão', 200, 5.80),
('Óleo', 80, 8.40),
('Açúcar', 120, 4.20);

#Consulta: Liste os produtos com quantidade abaixo de um valor mínimo.
SELECT * FROM produtos
WHERE quantidade < 100;

#Atualização: Atualize a quantidade de um produto após venda.
UPDATE produtos
SET quantidade = quantidade - 10
WHERE id = 1;

#Exclusão: Exclua um produto do estoque.
DELETE FROM produtos
WHERE id = 5;
