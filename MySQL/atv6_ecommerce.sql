/* O professor passou um banco de dados com vários erros para a turma e nos desafiou a encontrar e corrigir todos eles. 
Foi como um "jogo dos sete erros" — só que com bem mais de sete! 
Após revisar e corrigir os problemas de sintaxe, lógica e estrutura, o banco ficou assim: */


#drop database ecommerce;

# "datbase" deveria ser "database"
create database ecommerce;  

use ecommerce;

---------------------------------------------

create table produtos (
    id_prod int auto_increment not null,  
    nome_prod varchar(100) not null,  
    descricao text,  
    modelo varchar(50) not null,  
    id_categoria int,  
    id_fabricante int,  -- Vírgula corrigida
    constraint primary key (id_prod)
);

create table clientes (
    id_cli int auto_increment,  # `char` não pode ter `auto_increment`, usar `int`
    nome varchar(100) not null,  
    cpf varchar(11) not null,  # CPF pode começar com zero e `int` não mantém zeros à esquerda, melhor usar `varchar(11)`
    telefone varchar(50) not null,  
    sexo enum('F','M'),  
    cadastro datetime,  
    constraint primary key (id_cli)
); 

create table pedidos (
    num_pedido int auto_increment not null,  
    data datetime,  
    status varchar(50) not null,  
    id_cli int,  
    constraint primary key (num_pedido),  
    constraint foreign key (id_cli) references clientes(id_cli)  
);

# "tabe" deveria ser "table"
create table pedido_item (  
    id_item_pedido int auto_increment not null,  # "idtem_pedido" deveria ser "id_item_pedido"
    num_pedido int not null,  
    qtde int not null,  
    valor_unit decimal(10,2),  
    total decimal(10,2),  
    id_prod int,  
    constraint primary key (id_item_pedido),  
    # "foreing" deveria ser "foreign"
    constraint foreign key (num_pedido) references pedidos(num_pedido),  
    constraint foreign key (id_prod) references produtos(id_prod)  
);

create table estoque_produtos (
    id_estoque int auto_increment,  
    quantidade int not null,  
    quant_min int,  
    id_prod int,  # falta um fechamento de parêntese ")"
    constraint primary key (id_estoque),  
    constraint foreign key (id_prod) references produtos(id_prod)  
);

# "cliente" deveria ser "clientes"
insert into clientes values (null,'João','02102202324','6799999999','M',now());  
# "inset" deveria ser "insert"
insert into clientes values (null,'Tadeu','02102202366','6799999999','M',now());  
insert into clientes values (null,'Francisco','02102202399','6799999999','M',now());  
insert into clientes values (null,'Maria','02102202377','6799999999','F',now());  
insert into clientes values (null,'Antonia','02102202388','6799999999','F',now());  

insert into produtos values (null,'Notebook Dell','Core i5,8GB,SDD 240GB','Inspirion 1500',null,null);  
insert into produtos values (null,'Notebook Acer','Core i5,8GB,SDD 240GB','Aspire T',null,null);  
insert into produtos values (null,'Notebook Asus','Core i5,8GB,SDD 240GB','A95Z',null,null);  
insert into produtos values (null,'Notebook Apple','Core i7, 16GB, SDD 512GB','BookPRo',null,null);  
insert into produtos values (null,'Notebook Positivo','Celerom,4GB,HD 1TB','POS8080',null,null);  

insert into produtos values (null,'Placa-Mãe ASUS','Onboard','P',null,null);  
# nome do produto não está entre aspas
insert into produtos values (null,'Processador AMD','4.2Ghz','Ryzen5',null,null);  

insert into produtos values (null,'Placa de Vídeo RADEON','8GB','RX5500',null,null);  
# CX1200W não está entre aspas
insert into produtos values (null,'Fonte Corsair','Selo 80plus','CX1200W',null,null);  

select * from produtos;  
# "describle" deveria ser "describe"
describe estoque_produtos;  

insert into estoque_produtos values (null,80,10,1);  
# "estoque_produto" deveria ser "estoque_produtos"
insert into estoque_produtos values (null,44,5,9);  
insert into estoque_produtos values (null,55,5,8);  
insert into estoque_produtos values (null,36,5,7);  
insert into estoque_produtos values (null,49,5,6);  
insert into estoque_produtos values (null,100,5,1);  
insert into estoque_produtos values (null,100,5,2);  
insert into estoque_produtos values (null,100,5,3);  
insert into estoque_produtos values (null,100,5,4);  
insert into estoque_produtos values (null,100,5,5);  


