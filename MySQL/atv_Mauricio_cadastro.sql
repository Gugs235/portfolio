create database atv_Mauricio_cadastro;
use atv_Mauricio_cadastro;

create table nome (
id int primary key auto_increment,
nome varchar(80) not null

);

create table email (
id int primary key auto_increment,
email varchar(80) not null

);

create table endereco (
id int primary key auto_increment,
endereço varchar(80) not null

);

create table data_nascimento (
id int primary key auto_increment,
data_nascimento date not null

);

create table telefone (
id int primary key auto_increment,
telefone varchar(20) not null

);

create table cpf (
id int primary key auto_increment,
cpf varchar(15) not null

)

