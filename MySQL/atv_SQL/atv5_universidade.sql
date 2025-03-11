create database atv5_universidade;
use atv5_universidade;

create table departamento (
	código int primary key auto_increment,
	nome varchar(50),
    telefone varchar(15), 
	centro int
);

create table aluno(
	id int primary key auto_increment,
    matricula int,
    cpf varchar(20),
    rua varchar(50),
    cidade varchar(50),
    cep varchar(50),
    telefone varchar(15),
    celular varchar(15),
    data_nascimento date,
    sexo varchar(20),
    departamento varchar(50),
    curso varchar(50)
);

create table tipo_curso(
	id int primary key auto_increment,
    tipo varchar(50)
);

insert into tipo_curso (id, tipo) values 
(null, "técnico"),
(null, "graduação"),
(null, "mestrado "),
(null, "doutorado");

create table curso(
	nome varchar(50),
    id_tipo int,
    foreign key (id_tipo) references tipo_curso (tipo)
);
