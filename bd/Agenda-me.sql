CREATE SCHEMA agendame;
USE agendame;

create table usuarios(
	usuario char (30) primary key not null,
	nombre char (50),
    apellidos char (100),
    contraseña char (100)
);

create table eventos(
	id int primary key auto_increment,
    usuario char (30) not null,
    titulo char (40),
    descripcion varchar(200),
    dia char (20),
    fecha date,
    hora time,
	foreign key (usuario) references usuarios (usuario)
);