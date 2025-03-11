#3. Cadastro de Funcionários em uma Empresa
#Objetivo: Criar um banco de dados de funcionários.

create database atv14_CadastroFuncionarios;
use atv14_CadastroFuncionarios;

#Crie as tabelas funcionarios (id, nome, cargo, salario).
CREATE TABLE funcionarios (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nome VARCHAR(50) NOT NULL,
    cargo VARCHAR(50) NOT NULL,
    salario FLOAT NOT NULL
);

#Inserção: Insira registros de funcionários.
INSERT INTO funcionarios (nome, cargo, salario) VALUES
('João Silva', 'Analista de Sistemas', 4000.00),
('Maria Oliveira', 'Gerente de Projetos', 8000.00),
('Carlos Pereira', 'Desenvolvedor', 3500.00),
('Ana Santos', 'Analista de Suporte', 3000.00),
('Lucas Costa', 'Coordenador de TI', 9000.00);

#Consulta: Liste todos os funcionários com salário maior que um valor específico.
SELECT id, nome, cargo, salario
FROM funcionarios
WHERE salario > 4000.00;

#Atualização: Aumente o salário de um funcionário específico.
SET SQL_SAFE_UPDATES = 0;

UPDATE funcionarios
SET salario = salario * 1.10  -- Aumenta o salário em 10%
WHERE nome = 'Carlos Pereira';

#Exclusão: Exclua um funcionário da empresa.
DELETE FROM funcionarios
WHERE nome = 'Ana Santos';

SET SQL_SAFE_UPDATES = 1;
