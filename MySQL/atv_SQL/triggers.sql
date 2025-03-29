create database aula_trigger;
use aula_trigger;

create table produto(
referencial varchar(3) primary key,
descricao varchar(50) unique,
estoque int not null default 0

);

insert into produto values ('001', 'feijão', 10);
insert into produto values ('002', 'arroz', 5);
insert into produto values ('003', 'farinha', 15);

create table item_venda (
venda int,
produto varchar(3),
quantidade int,
foreign key (produto) references produto (referencial)

);

insert into item_venda values ('1', '001', 3);
insert into item_venda values ('2', '002', 1);
insert into item_venda values ('3', '003', 5);

select * from item_venda;
delete from item_venda where venda = 1 and produto = '001';

delimiter $
create trigger tgr_item_venda_Insert after insert
on item_venda
for each row
begin
update produto set estoque = estoque - new.quantidade
where referencial = new.produto;
end$

delimiter ;

insert into item_venda values ('4', '001', 3);
insert into item_venda values ('5', '002', 1);
insert into item_venda values ('6', '003', 5);

delimiter $
create trigger tgr_item_venda_delet after delete
on item_venda
for each row
begin
update produto set estoque = estoque + old.quantidade
where referencial = old.produto;
end$
delimiter ;

delete from item_venda where venda = 1;

select * from item_venda;
select * from produto;

SET SQL_SAFE_UPDATES = 0;

#show triggers;
#drop trigger nome da trigger