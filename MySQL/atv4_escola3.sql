# O código SQL cria um banco de dados chamado atv4_escola3 e define tabelas para armazenar informações sobre alunos, estados e cidades. 
# Ele estabelece relações entre estados e cidades, vinculando cada cidade ao seu respectivo estado.


create database atv4_escola3;
use atv4_escola3;

create table aluno (
	matricula int primary key auto_increment,
    nome varchar(50) not null,
    email varchar(50) not null
);

insert into aluno (matricula, nome, email) values (null, "Jhonathan", "jhon@soares"),
(null, "Anne", "anne@primon"),
(null, "Celso", "celso@primon"),
(null, "Luiz", "luiz@aluno"),
(null, "Igor", "Igor@aluno");

create table estado (
	id int primary key auto_increment,
	nome_estado varchar(50) not null,
    sigla varchar(50) not null
);

insert into estado (id, nome_estado, sigla) values (null, "Acre", "AC"),  
(null, "Alagoas", "AL"),  
(null, "Amapá", "AP"),  
(null, "Amazonas", "AM"),  
(null, "Bahia", "BA"),  
(null, "Ceará", "CE"),  
(null, "Distrito Federal", "DF"),  
(null, "Espírito Santo", "ES"),  
(null, "Goiás", "GO"),  
(null, "Maranhão", "MA"),  
(null, "Mato Grosso", "MT"),  
(null, "Mato Grosso do Sul", "MS"),  
(null, "Minas Gerais", "MG"),  
(null, "Pará", "PA"),  
(null, "Paraíba", "PB"),  
(null, "Paraná", "PR"),  
(null, "Pernambuco", "PE"),  
(null, "Piauí", "PI"),  
(null, "Rio de Janeiro", "RJ"),  
(null, "Rio Grande do Norte", "RN"),  
(null, "Rio Grande do Sul", "RS"),  
(null, "Rondônia", "RO"),  
(null, "Roraima", "RR"),  
(null, "Santa Catarina", "SC"),  
(null, "São Paulo", "SP"),  
(null, "Sergipe", "SE"),  
(null, "Tocantins", "TO"); 

create table cidade (
	id int primary key auto_increment,
	nome varchar(50) not null,
    id_estado int not null,
    foreign key (id_estado)references estado (id),
    região varchar(50) not null
);

insert into cidade (id, nome, id_estado, região) values  
(null, "São Paulo", 12, "Sudeste"),  
(null, "Rio de Janeiro", 7, "Sudeste"),  
(null, "Belo Horizonte", 19, "Sudeste"),  
(null, "Vitória", 3, "Sudeste"),  
(null, "Curitiba", 25, "Sul"),  
(null, "Porto Alegre", 8, "Sul"),  
(null, "Florianópolis", 14, "Sul"),  
(null, "Salvador", 22, "Nordeste"),  
(null, "Recife", 6, "Nordeste"),  
(null, "Fortaleza", 17, "Nordeste"),  
(null, "São Luís", 9, "Nordeste"),  
(null, "Natal", 1, "Nordeste"),  
(null, "João Pessoa", 16, "Nordeste"),  
(null, "Brasília", 27, "Centro-Oeste"),  
(null, "Goiânia", 11, "Centro-Oeste"),  
(null, "Cuiabá", 4, "Centro-Oeste"),  
(null, "Campo Grande", 20, "Centro-Oeste"),  
(null, "Manaus", 2, "Norte"),  
(null, "Belém", 13, "Norte"),  
(null, "Palmas", 23, "Norte");  


# ver uma tabela - select * from "nome da tabela";
# apagar - drop table "nome da tabela";
