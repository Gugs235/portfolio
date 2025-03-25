create database atv17_triggers;
USE atv17_triggers;


create table Estado (
    id_estado int auto_increment primary key,
    nome varchar(50) not null,
    sigla char(2) not null
);

create table Cidade (
    id_cidade int auto_increment primary key,
    nome varchar(50) not null,
    id_estado int,
    foreign key(id_estado) references Estado(id_estado)
);

create table Gênero (
    id_genero int auto_increment primary key,
    descricao varchar(20) not null
);

create table Raça (
    id_raca int auto_increment primary key,
    descricao varchar(20) not null
);

create table Religião (
    id_religiao int auto_increment primary key,
    descricao varchar(50) not null
);

create table Agências (
    id_agencia int auto_increment primary key,
    numero_agencia varchar(10) not null,
    endereco varchar(100) not null,
    id_cidade int,
    id_estado int,
    foreign key (id_cidade) references Cidade(id_cidade),
    foreign key (id_estado) references Estado(id_estado)
);

create table Clientes (
    id_cliente int auto_increment primary key,
    nome varchar(100) not null,
    id_cidade int,
    id_estado int,
    id_genero int,
    id_raca int,
    id_religiao int,
    id_agencia int,
    numero_conta varchar(20) unique not null,
    saldo decimal(10,2) default 0,
    foreign key (id_cidade) references Cidade(id_cidade),
    foreign key (id_estado) references Estado(id_estado),
    foreign key (id_genero) references Gênero(id_genero),
    foreign key (id_raca) references Raça(id_raca),
    foreign key (id_religiao) references Religião(id_religiao),
    foreign key (id_agencia) references Agências(id_agencia)
);

create table Saque (
    id_saque int auto_increment primary key,
    id_agencia int,
    id_conta int,
    valor decimal(10,2) not null,
    data_hora timestamp default current_timestamp,
    foreign key (id_agencia) references Agências(id_agencia),
    foreign key (id_conta) references Clientes(id_cliente)
);

create table Deposito (
    id_deposito int auto_increment primary key,
    id_agencia int,
    id_conta int,
    valor decimal(10,2) not null,
    data_hora timestamp default current_timestamp,
    foreign key (id_agencia) references Agências(id_agencia),
    foreign key (id_conta) references Clientes(id_cliente)
);

delimiter $
create trigger tgr_saque_insert
after insert on Saque
for each row
begin
    update Clientes set saldo = saldo - new.valor where id_cliente = new.id_conta;
end $
delimiter ;

delimiter $
create trigger tgr_deposito_insert
after insert on Deposito
for each row
begin
    update Clientes set saldo = saldo + new.valor WHERE id_cliente = new.id_conta;
end $
delimiter ;
