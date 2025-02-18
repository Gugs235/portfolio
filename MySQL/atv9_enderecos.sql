/*instruções
Crie um banco de dados, que contenha uma tabela endereço, que irá buscar os dados das seguintes tabelas: Rua, Bairro, Cidade, Estado, País, Continente.

Rua: 50 registros
Bairro: 30 Registros
Cidade: 30 Registros
Estado: 30 Registros
País: 15 Registros
Continente: 5 Registros*/;


create database atv9_enderecos;
use atv9_enderecos;

create table continente (
	id int primary key auto_increment,
    nome_continente varchar(50) not null
);

create table pais (
	id int primary key auto_increment,
    nome_pais varchar(50) not null,
    continente_id int,
    foreign key (continente_id) references continente(id)
);

create table estado (
	id int primary key auto_increment,
    nome_estado varchar(50) not null,
    pais_id int,
    foreign key (pais_id) references pais(id)
);

create table cidade (
	id int primary key auto_increment,
    nome_cidade varchar(50) not null,
    estado_id int,
    foreign key (estado_id) references estado(id)
);

create table bairro (
	id int primary key auto_increment,
    nome_bairro varchar(50) not null,
    cidade_id int,
    foreign key (cidade_id) references cidade(id)
);

create table rua (
	id int primary key auto_increment,
    nome_rua varchar(50) not null,
    rua_id int,
    foreign key (rua_id) references bairro(id)
);

create table endereco (
	id int primary key auto_increment,
    rua_id int,
    bairro_id int,
    cidade_id int,
    estado_id int,
    pais_id int,
    continente_id int,
    foreign key (rua_id) references bairro(id),
	foreign key (bairro_id) references bairro(id),
    foreign key (cidade_id) references cidade(id),
    foreign key (estado_id) references estado(id),
    foreign key (pais_id) references pais(id),
    foreign key (continente_id) references continente(id)
);

insert into continente (nome_continente) values
("América do Norte"),  
("América do Sul"),  
("Europa"),  
("Ásia"),  
("África");

insert into pais (nome_pais) values
("Brasil"),  
("Estados Unidos"),  
("Canadá"),  
("Argentina"),  
("México"),  
("França"),  
("Alemanha"),  
("Itália"),  
("Espanha"),  
("Japão"),  
("China"),  
("Rússia"),  
("Austrália"),  
("Índia"),  
("África do Sul"),
("Portugal"),  
("Suécia"),  
("Noruega"),  
("Finlândia"),  
("Coreia do Sul"),  
("Egito"),  
("Chile"),  
("Colômbia"),  
("Turquia"),  
("Nova Zelândia");


insert into estado (nome_estado) values
("São Paulo"),  
("Rio de Janeiro"),  
("Minas Gerais"),  
("Bahia"),  
("Paraná"),  
("Santa Catarina"),  
("Rio Grande do Sul"),  
("Goiás"),  
("Pernambuco"),  
("Ceará"),  
("Amazonas"),  
("Pará"),  
("Maranhão"),  
("Mato Grosso"),  
("Espírito Santo"),  
("Tocantins"),  
("Acre"),  
("Roraima"),  
("Amapá"),  
("Piauí"),  
("Alagoas"),  
("Sergipe"),  
("Rio Grande do Norte"),  
("Paraíba"),  
("Mato Grosso do Sul"),  
("Rondônia"),  
("Distrito Federal"),  
("Nova York"),  
("Califórnia"),  
("Ontário");

insert into cidade (nome_cidade) values
("São Paulo"),  
("Rio de Janeiro"),  
("Belo Horizonte"),  
("Salvador"),  
("Curitiba"),  
("Florianópolis"),  
("Porto Alegre"),  
("Goiânia"),  
("Recife"),  
("Fortaleza"),  
("Manaus"),  
("Belém"),  
("São Luís"),  
("Cuiabá"),  
("Vitória"),  
("Palmas"),  
("Rio Branco"),  
("Boa Vista"),  
("Macapá"),  
("Teresina"),  
("Maceió"),  
("Aracaju"),  
("Natal"),  
("João Pessoa"),  
("Campo Grande"),  
("Porto Velho"),  
("Brasília"),  
("Nova York"),  
("Los Angeles"),  
("Toronto");

insert into bairro (nome_bairro) values
("Vila Mariana"),  
("Pinheiros"),  
("Moema"),  
("Copacabana"),  
("Leblon"),  
("Barra da Tijuca"),  
("Boa Viagem"),  
("Caminho das Árvores"),  
("Cidade Nova"),  
("Centro"),  
("Santa Cecília"),  
("Itaim Bibi"),  
("Santana"),  
("Lapa"),  
("Tatuapé"),  
("Vila Isabel"),  
("Botafogo"),  
("Tijuca"),  
("Flamengo"),  
("Madureira"),  
("Asa Sul"),  
("Asa Norte"),  
("Noroeste"),  
("Alphaville"),  
("São Conrado"),  
("Pampulha"),  
("Buritis"),  
("Sudoeste"),  
("Lago Sul"),  
("Lago Norte");

insert into rua (nome_rua) values
("Rua das Palmeiras"),  
("Avenida Paulista"),  
("Rua XV de Novembro"),  
("Rua das Flores"),  
("Rua das Laranjeiras"),  
("Rua da Consolação"),  
("Avenida Atlântica"),  
("Rua Augusta"),  
("Rua do Comércio"),  
("Rua Sete de Setembro"),  
("Rua Marechal Deodoro"),  
("Rua dos Andradas"),  
("Rua Barão de Itapetininga"),  
("Rua Visconde de Pirajá"),  
("Avenida Brasil"),  
("Rua do Catete"),  
("Rua Voluntários da Pátria"),  
("Rua Domingos Ferreira"),  
("Avenida Getúlio Vargas"),  
("Rua Santa Catarina"),  
("Rua Benjamin Constant"),  
("Rua General Osório"),  
("Rua Peixoto Gomide"),  
("Rua João Pessoa"),  
("Rua São José"),  
("Avenida Copacabana"),  
("Rua do Passeio"),  
("Rua Henrique Schaumann"),  
("Avenida das Américas"),  
("Rua Tupinambás"),  
("Rua Jorge Amado"),  
("Rua Santo Antônio"),  
("Rua Doutor Arnaldo"),  
("Rua Professor Moraes"),  
("Rua Silva Jardim"),  
("Rua dos Bandeirantes"),  
("Rua 25 de Março"),  
("Avenida Ibirapuera"),  
("Avenida João XXIII"),  
("Rua Senador Dantas"),  
("Avenida República do Líbano"),  
("Rua Almirante Tamandaré"),  
("Rua Carlos Gomes"),  
("Rua Pedro Álvares Cabral"),  
("Rua da Liberdade"),  
("Rua das Nações Unidas"),  
("Rua Martins Fontes"),  
("Avenida Washington Luís"),  
("Rua Doutor Osvaldo Cruz"),  
("Rua Miguel de Cervantes");

/*Faça as seguintes consulta:

Qual é a rua de ID nº 37
Qual é o bairro de ID nº 12
Qual é a cidade de ID nº 29
Qual é o estado de ID nº 9
Qual é o país de ID nº 19
Qual o continente de ID nº 4
*/;

select id,nome_rua FROM rua WHERE id = 37;
select id,nome_bairro FROM bairro WHERE id = 12;
select id,nome_cidade FROM cidade WHERE id = 29;
select id,nome_estado FROM estado WHERE id = 9;
select id,nome_pais FROM pais WHERE id = 19;
select id,nome_continente FROM continente WHERE id = 4;


/*Agora, adicione o campo população, sem dropar a tabela,  em cada um dos países, em cada um dos continentes, em cada um dos estados, em cada uma das cidades.*/
alter table pais 
modify populacao varchar(30);
alter table continente
modify populacao varchar(30);
alter table estado
modify populacao varchar(30);
alter table cidade 
modify populacao varchar(30);

insert into continente (id, nome_continente, populacao) values
(null,"América do Norte", "579.000.000"),
(null,"América do Sul ", "430.000.000"),
(null,"Europa", "747.000.000"),
(null,"Ásia", "4.600.000.000"),
(null,"África","1.400.000.000");

insert into pais (id, nome_pais, populacao) values
(null, "Brasil", "214.000.000"),  
(null, "Estados Unidos", "331.893.000"),  
(null, "Canadá", "38.067.000"),  
(null, "Argentina", "45.376.000"),  
(null, "México", "130.262.000"),  
(null, "França", "67.084.000"),  
(null, "Alemanha", "83.883.000"),  
(null, "Itália", "60.417.000"),  
(null, "Espanha", "47.615.000"),  
(null, "Japão", "125.584.000"),  
(null, "China", "1.425.000.000"),  
(null, "Rússia", "145.805.000"),  
(null, "Austrália", "25.687.000"),  
(null, "Índia", "1.428.000.000"),  
(null, "África do Sul", "60.141.000");

insert into estado (id, nome_estado, populacao) values
(null, "São Paulo", "46.289.333"),  
(null, "Rio de Janeiro", "17.366.189"),  
(null, "Minas Gerais", "21.290.000"),  
(null, "Bahia", "15.127.524"),  
(null, "Paraná", "11.516.840"),  
(null, "Santa Catarina", "7.338.473"),  
(null, "Rio Grande do Sul", "11.370.000"),  
(null, "Goiás", "7.112.537"),  
(null, "Pernambuco", "9.674.000"),  
(null, "Ceará", "9.084.000"),  
(null, "Amazonas", "4.269.000"),  
(null, "Pará", "8.622.000"),  
(null, "Maranhão", "7.117.000"),  
(null, "Mato Grosso", "3.482.000"),  
(null, "Espírito Santo", "4.063.000"),  
(null, "Tocantins", "1.590.000"),  
(null, "Acre", "892.000"),  
(null, "Roraima", "652.000"),  
(null, "Amapá", "861.000"),  
(null, "Piauí", "3.284.000"),  
(null, "Alagoas", "3.349.000"),  
(null, "Sergipe", "2.350.000"),  
(null, "Rio Grande do Norte", "3.598.000"),  
(null, "Paraíba", "4.039.000"),  
(null, "Mato Grosso do Sul", "2.849.000"),  
(null, "Rondônia", "2.402.000"),  
(null, "Distrito Federal", "3.100.000"),  
(null, "Nova York", "19.798.000"),  
(null, "Califórnia", "39.512.000"),  
(null, "Ontário", "13.448.000");


insert into cidade (id, nome_cidade, populacao) values
(null, "São Paulo", "12.396.000"),  
(null, "Rio de Janeiro", "6.747.815"),  
(null, "Belo Horizonte", "2.530.701"),  
(null, "Salvador", "2.900.319"),  
(null, "Curitiba", "1.948.626"),  
(null, "Florianópolis", "508.826"),  
(null, "Porto Alegre", "1.484.941"),  
(null, "Goiânia", "1.516.714"),  
(null, "Recife", "1.653.461"),  
(null, "Fortaleza", "2.669.000"),  
(null, "Manaus", "2.220.000"),  
(null, "Belém", "1.499.000"),  
(null, "São Luís", "1.100.000"),  
(null, "Cuiabá", "618.000"),  
(null, "Vitória", "365.000"),  
(null, "Palmas", "305.000"),  
(null, "Rio Branco", "413.000"),  
(null, "Boa Vista", "406.000"),  
(null, "Macapá", "512.000"),  
(null, "Teresina", "864.000"),  
(null, "Maceió", "1.025.000"),  
(null, "Aracaju", "657.000"),  
(null, "Natal", "1.350.000"),  
(null, "João Pessoa", "817.000"),  
(null, "Campo Grande", "900.000"),  
(null, "Porto Velho", "518.000"),  
(null, "Brasília", "3.039.000"),  
(null, "Nova York", "8.336.817"),  
(null, "Los Angeles", "3.990.000"),  
(null, "Toronto", "2.731.571");


/*Qual País, Continente, Estado e Cidade possui a maior e menor população.*/

SELECT * FROM pais ORDER BY populacao DESC LIMIT 10;
SELECT * FROM pais ORDER BY populacao ASC LIMIT 10;

SELECT * FROM continente ORDER BY populacao DESC LIMIT 10;
SELECT * FROM continente ORDER BY populacao ASC LIMIT 10;

SELECT * FROM estado ORDER BY populacao DESC LIMIT 10;
SELECT * FROM estado ORDER BY populacao ASC LIMIT 10;

SELECT * FROM cidade ORDER BY populacao DESC LIMIT 10;
SELECT * FROM cidade ORDER BY populacao ASC LIMIT 10;
