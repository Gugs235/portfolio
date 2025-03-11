#2. Sistema de Gestão de Alunos
#Objetivo: Criar um banco de dados para gerenciar alunos e suas notas.

create database atv13_GestãoDeAlunos;
use atv13_GestãoDeAlunos;

#Crie as tabelas alunos (id, nome, idade) e notas (id, aluno_id, disciplina, nota).
create table alunos (
id int primary key auto_increment not null,
nome_alunos varchar(50) not null,
idade int not null
);

create table notas (
id int primary key auto_increment not null,
aluno_id int,
disciplina varchar(50) not null,
nota float not null,
foreign key (aluno_id) references alunos (id)
); 

#Inserção: Adicione alguns alunos e suas notas.
INSERT INTO alunos (nome_alunos, idade) VALUES
('João Silva', 16),
('Maria Oliveira', 17),
('Carlos Pereira', 18),
('Ana Santos', 15),
('Lucas Costa', 17);

INSERT INTO notas (aluno_id, disciplina, nota) VALUES
(1, 'Matemática', 8.5),
(1, 'Português', 7.0),
(2, 'Matemática', 9.0),
(2, 'Português', 8.5),
(3, 'Matemática', 6.5),
(3, 'Português', 7.5),
(4, 'Matemática', 9.5),
(4, 'Português', 9.0),
(5, 'Matemática', 7.0),
(5, 'Português', 8.0);

#Consulta: Consulte as notas de um aluno específico.
SELECT alunos.id, alunos.nome_alunos, alunos.idade, notas.disciplina, notas.nota
FROM alunos
INNER JOIN notas ON alunos.id = notas.aluno_id
WHERE alunos.nome_alunos = 'João Silva';

#Atualização: Atualize a nota de um aluno em uma disciplina.
UPDATE notas
SET nota = 5
WHERE aluno_id = (SELECT id FROM alunos WHERE nome_alunos = 'João Silva')
AND disciplina = 'Matemática';

#Exclusão: Exclua a nota de um aluno em uma disciplina.
DELETE FROM notas
WHERE aluno_id = (SELECT id FROM alunos WHERE nome_alunos = 'João Silva')
AND disciplina = 'Matemática';

#Adicionando: Adicione a nota de um aluno em uma disciplina.
INSERT INTO notas (aluno_id, disciplina, nota)
VALUES ((SELECT id FROM alunos WHERE nome_alunos = 'João Silva'), 'Matemática', 8.5);

#Mostrando tudo: mostre todos os alunos e suas idades com todas as suas matérias e notas
SELECT alunos.id, alunos.nome_alunos, alunos.idade, notas.disciplina, notas.nota
FROM alunos
INNER JOIN notas ON alunos.id = notas.aluno_id;
