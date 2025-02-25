create database atv10_cadastro;
use atv10_cadastro;

create table escolaridade (
id_escolaridade int primary key auto_increment,
nome_escolaridade varchar(50)

);

create table raca (
id_raca int primary key auto_increment,
nome_raca varchar(50)

);

create table nacionalidade (
id_nacionalidade int primary key auto_increment,
nome_nacionalidade varchar(50)

);

create table sexo (
id_sexo int primary key auto_increment,
nome_sexo varchar(50)

);

create table estado (
id_estado int primary key auto_increment,
nome_estado varchar(50)

);

create table cidade (
id_cidade int primary key auto_increment,
nome_cidade varchar(50),
id_estado int,
foreign key (id_estado) references estado(id_estado)
);

create table cadastro_cliente (
id int primary key auto_increment,
nome varchar(50),
cpf varchar(15) UNIQUE,
rg varchar(20) UNIQUE,
telefone varchar(20),
id_escolaridade int,
id_raca int,
id_cidade int,
id_sexo int,
id_nacionalidade int,
foreign key (id_cidade) references cidade(id_cidade),
foreign key (id_sexo) references sexo(id_sexo),
foreign key (id_nacionalidade) references nacionalidade(id_nacionalidade),
foreign key (id_escolaridade) references escolaridade(id_escolaridade),
foreign key (id_raca) references raca(id_raca)
);

-- Inserir estados do Brasil
INSERT INTO estado (nome_estado) VALUES
('Acre'), ('Alagoas'), ('Amapá'), ('Amazonas'), ('Bahia'),
('Ceará'), ('Distrito Federal'), ('Espírito Santo'), ('Goiás'),
('Maranhão'), ('Mato Grosso'), ('Mato Grosso do Sul'), ('Minas Gerais'),
('Pará'), ('Paraíba'), ('Paraná'), ('Pernambuco'), ('Piauí'),
('Rio de Janeiro'), ('Rio Grande do Norte'), ('Rio Grande do Sul'),
('Rondônia'), ('Roraima'), ('Santa Catarina'), ('São Paulo'),
('Sergipe'), ('Tocantins');

-- Inserir 5 cidades para cada estado
INSERT INTO cidade (nome_cidade, id_estado) VALUES
-- Acre
('Rio Branco', 1), ('Cruzeiro do Sul', 1), ('Sena Madureira', 1), ('Tarauacá', 1), ('Feijó', 1),
-- Alagoas
('Maceió', 2), ('Arapiraca', 2), ('Palmeira dos Índios', 2), ('Rio Largo', 2), ('Penedo', 2),
-- Amapá
('Macapá', 3), ('Santana', 3), ('Laranjal do Jari', 3), ('Oiapoque', 3), ('Mazagão', 3),
-- Amazonas
('Manaus', 4), ('Parintins', 4), ('Itacoatiara', 4), ('Manacapuru', 4), ('Tefé', 4),
-- Bahia
('Salvador', 5), ('Feira de Santana', 5), ('Vitória da Conquista', 5), ('Camaçari', 5), ('Juazeiro', 5),
-- Ceará
('Fortaleza', 6), ('Juazeiro do Norte', 6), ('Sobral', 6), ('Maracanaú', 6), ('Iguatu', 6),
-- Distrito Federal
('Brasília', 7), ('Ceilândia', 7), ('Taguatinga', 7), ('Samambaia', 7), ('Planaltina', 7),
-- Espírito Santo
('Vitória', 8), ('Vila Velha', 8), ('Serra', 8), ('Cariacica', 8), ('Guarapari', 8),
-- Goiás
('Goiânia', 9), ('Aparecida de Goiânia', 9), ('Anápolis', 9), ('Rio Verde', 9), ('Luziânia', 9),
-- Maranhão
('São Luís', 10), ('Imperatriz', 10), ('Caxias', 10), ('Timon', 10), ('Codó', 10),
-- Mato Grosso
('Cuiabá', 11), ('Várzea Grande', 11), ('Rondonópolis', 11), ('Sinop', 11), ('Lucas do Rio Verde', 11),
-- Mato Grosso do Sul
('Campo Grande', 12), ('Dourados', 12), ('Três Lagoas', 12), ('Corumbá', 12), ('Ponta Porã', 12),
-- Minas Gerais
('Belo Horizonte', 13), ('Uberlândia', 13), ('Contagem', 13), ('Juiz de Fora', 13), ('Betim', 13),
-- Pará
('Belém', 14), ('Ananindeua', 14), ('Santarém', 14), ('Marabá', 14), ('Castanhal', 14),
-- Paraíba
('João Pessoa', 15), ('Campina Grande', 15), ('Santa Rita', 15), ('Patos', 15), ('Bayeux', 15),
-- Paraná
('Curitiba', 16), ('Londrina', 16), ('Maringá', 16), ('Cascavel', 16), ('Ponta Grossa', 16),
-- Pernambuco
('Recife', 17), ('Jaboatão dos Guararapes', 17), ('Olinda', 17), ('Caruaru', 17), ('Petrolina', 17),
-- Piauí
('Teresina', 18), ('Parnaíba', 18), ('Picos', 18), ('Floriano', 18), ('Piripiri', 18),
-- Rio de Janeiro
('Rio de Janeiro', 19), ('São Gonçalo', 19), ('Duque de Caxias', 19), ('Nova Iguaçu', 19), ('Niterói', 19),
-- Rio Grande do Norte
('Natal', 20), ('Mossoró', 20), ('Parnamirim', 20), ('São Gonçalo do Amarante', 20), ('Macau', 20),
-- Rio Grande do Sul
('Porto Alegre', 21), ('Caxias do Sul', 21), ('Pelotas', 21), ('Santa Maria', 21), ('Gravataí', 21),
-- Rondônia
('Porto Velho', 22), ('Ji-Paraná', 22), ('Ariquemes', 22), ('Cacoal', 22), ('Vilhena', 22),
-- Roraima
('Boa Vista', 23), ('Rorainópolis', 23), ('Caracaraí', 23), ('Mucajaí', 23), ('Pacaraima', 23),
-- Santa Catarina
('Florianópolis', 24), ('Joinville', 24), ('Blumenau', 24), ('São José', 24), ('Chapecó', 24),
-- São Paulo
('São Paulo', 25), ('Guarulhos', 25), ('Campinas', 25), ('São Bernardo do Campo', 25), ('Osasco', 25),
-- Sergipe
('Aracaju', 26), ('Nossa Senhora do Socorro', 26), ('Lagarto', 26), ('Itabaiana', 26), ('Estância', 26),
-- Tocantins
('Palmas', 27), ('Araguaína', 27), ('Gurupi', 27), ('Porto Nacional', 27), ('Paraíso do Tocantins', 27);

-- Inserir tipos de sexo
INSERT INTO sexo (nome_sexo) VALUES
('Masculino'), ('Feminino'), ('Outro');

-- Inserir nacionalidades
INSERT INTO nacionalidade (nome_nacionalidade) VALUES
('Brasileira'), ('Estrangeira');

-- Inserir raças
INSERT INTO raca (nome_raca) VALUES
('Branca'), ('Preta'), ('Parda'), ('Amarela'), ('Indígena');

-- Inserir tipos de escolaridade
INSERT INTO escolaridade (nome_escolaridade) VALUES
('Ensino Fundamental Incompleto'), ('Ensino Fundamental Completo'),
('Ensino Médio Incompleto'), ('Ensino Médio Completo'),
('Ensino Superior Incompleto'), ('Ensino Superior Completo'),
('Pós-Graduação'), ('Mestrado');

-- Inserir 20 registros de clientes
INSERT INTO cadastro_cliente (nome, cpf, rg, telefone, id_escolaridade, id_raca, id_cidade, id_sexo, id_nacionalidade) VALUES
('Ana Maria', '123.456.789-00', 'MG-12.345.678', '31987654321', 4, 1, 1, 2, 1),
('Carlos Silva', '987.654.321-00', 'SP-87.654.321', '11987654321', 5, 2, 2, 1, 1),
('João Pedro', '456.789.123-00', 'RJ-45.678.912', '21987654321', 6, 3, 3, 1, 2),
('Mariana Lima', '321.654.987-00', 'RS-32.165.498', '51987654321', 7, 1, 4, 2, 1),
('Pedro Oliveira', '789.123.456-00', 'BA-78.912.345', '71987654321', 4, 2, 5, 1, 1),
('Beatriz Santos', '159.753.486-00', 'AM-15.975.348', '92987654321', 5, 3, 6, 2, 1),
('Lucas Almeida', '357.951.852-00', 'CE-35.795.185', '85987654321', 6, 4, 7, 1, 1),
('Fernanda Costa', '753.852.159-00', 'SC-75.385.215', '48987654321', 8, 1, 8, 2, 1),
('Rafael Sousa', '951.753.258-00', 'PA-95.175.325', '91987654321', 4, 2, 9, 1, 2),
('Camila Rocha', '258.159.753-00', 'PE-25.815.975', '81987654321', 5, 3, 10, 2, 1),
('Vinícius Nunes', '852.456.159-00', 'PR-85.245.615', '41987654321', 6, 4, 11, 1, 1),
('Juliana Melo', '123.654.789-00', 'MG-12.365.478', '31987651234', 7, 1, 12, 2, 1),
('Fábio Martins', '456.321.987-00', 'SP-45.632.198', '11987653210', 8, 2, 13, 1, 1),
('Larissa Silva', '789.456.123-00', 'RJ-78.945.612', '21987654322', 4, 3, 14, 2, 1),
('Bruno Oliveira', '147.258.369-00', 'BA-14.725.836', '71987654323', 5, 1, 15, 1, 1),
('Gabriela Ferreira', '369.258.147-00', 'RS-36.925.814', '51987654324', 6, 2, 16, 2, 1),
('Thiago Almeida', '258.369.147-00', 'AM-25.836.914', '92987654325', 7, 3, 17, 1, 2),
('Isabela Santos', '147.369.258-00', 'CE-14.736.925', '85987654326', 8, 4, 18, 2, 1),
('Rafael Lima', '963.852.741-00', 'SC-96.385.274', '48987654327', 4, 1, 19, 1, 1),
('Luana Costa', '741.852.963-00', 'PA-74.185.296', '91987654328', 5, 2, 20, 2, 1);


SELECT id, nome, id_cidade FROM cadastro_cliente;


# apresentar um select com apenas o nome e a cidade
select cadastro_cliente.nome, cidade.nome_cidade 
FROM cadastro_cliente 
INNER JOIN cidade ON cadastro_cliente.id_cidade = cidade.id_cidade;

# apresentar um select com apenas o nome e a estado
select cadastro_cliente.nome, estado.nome_estado 
from cadastro_cliente 
join cidade on cadastro_cliente.id_cidade = cidade.id_cidade 
join estado on cidade.id_estado = estado.id_estado;

# apresentar um select com apenas o nome, cpf e raça
select cadastro_cliente.nome, cadastro_cliente.cpf, raca.nome_raca
from cadastro_cliente
join raca on cadastro_cliente.id_raca = raca.id_raca;

# apresentar um select com apenas o nome e a nacionalidade
select cadastro_cliente.nome, escolaridade.nome_escolaridade
from cadastro_cliente
join escolaridade on cadastro_cliente.id_escolaridade = escolaridade.id_escolaridade;

# apresentar um select com apenas o nome e a escolaridade
select cadastro_cliente.nome, nacionalidade.nome_nacionalidade
from cadastro_cliente
join nacionalidade on cadastro_cliente.id_nacionalidade = nacionalidade.id_nacionalidade;

# apresentar um select com apenas o nome, cidade e estado
select cadastro_cliente.nome, cidade.nome_cidade, estado.nome_estado
from cadastro_cliente
join cidade on cadastro_cliente.id_cidade = cidade.id_cidade
join estado on cidade.id_estado = estado.id_estado;

# apresentar um select com apenas o nome, cidade, estado, fone, rg, sexo, nacionalidade, raça, escolaridade
select cadastro_cliente.nome, cidade.nome_cidade, estado.nome_estado, cadastro_cliente.telefone, cadastro_cliente.rg, sexo.nome_sexo, nacionalidade.nome_nacionalidade, raca.nome_raca, escolaridade.nome_escolaridade
from cadastro_cliente
join cidade on cadastro_cliente.id_cidade = cidade.id_cidade
join estado on cidade.id_estado = estado.id_estado
join sexo on cadastro_cliente.id_sexo = sexo.id_sexo
join nacionalidade on cadastro_cliente.id_nacionalidade = nacionalidade.id_nacionalidade
join raca on cadastro_cliente.id_raca = raca.id_raca
join escolaridade on cadastro_cliente.id_escolaridade = escolaridade.id_escolaridade;

