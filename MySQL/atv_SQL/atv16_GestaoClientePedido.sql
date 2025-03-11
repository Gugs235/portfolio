#5. Gestão de Clientes e Pedidos
#Objetivo: Criar um banco de dados para gerenciar clientes e pedidos de uma loja.

create database atv16_GestaoClientePedido;
use atv16_GestaoClientePedido;

#Crie as tabelas clientes (id, nome, email), pedidos (id, cliente_id, data, total).
CREATE TABLE clientes (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
);

CREATE TABLE pedidos (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    cliente_id INT NOT NULL,
    data DATE NOT NULL,
    total FLOAT NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

#Inserção: Adicione clientes e seus pedidos.
INSERT INTO clientes (nome, email) VALUES
('João da Silva', 'joao.silva@email.com'),
('Maria Oliveira', 'maria.oliveira@email.com'),
('Carlos Pereira', 'carlos.pereira@email.com'),
('Ana Santos', 'ana.santos@email.com');

INSERT INTO pedidos (cliente_id, data, total) VALUES
(1, '2025-03-06', 150.75),
(1, '2025-03-07', 200.50),
(2, '2025-03-06', 99.99),
(3, '2025-03-06', 450.00),
(4, '2025-03-05', 75.25);

#Consulta: Liste os pedidos de um cliente específico.
SELECT clientes.nome, pedidos.id AS pedido_id, pedidos.data, pedidos.total
FROM clientes
INNER JOIN pedidos ON clientes.id = pedidos.cliente_id
WHERE clientes.nome = 'João da Silva';

#Atualização: Atualize o total de um pedido.
UPDATE pedidos
SET total = 180.00
WHERE id = 1;

#Exclusão: Exclua um pedido de um cliente.
DELETE FROM pedidos
WHERE id = 3;
