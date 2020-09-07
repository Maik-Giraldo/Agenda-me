CREATE SCHEMA agendame;
USE agendame;

create table usuarios(
	usuario char (30) primary key not null,
	nombre char (50) not null,
    apellidos char (100) not null,
    contraseña varbinary (20) not null
);

create table eventos(
	id_evento int primary key not null auto_increment,
    usuario char (30) not null,
    titulo char (40) not null,
    descripcion varchar(200),
    dia char (20) not null,
    fecha date not null,
    hora time not null,
    foreign key (usuario) references usuarios(usuario)
);