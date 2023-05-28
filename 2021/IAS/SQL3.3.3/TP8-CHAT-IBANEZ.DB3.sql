--
-- File generated with SQLiteStudio v3.3.3 on jue. jun. 10 16:17:31 2021
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: GRUPO_USUARIOS
CREATE TABLE GRUPO_USUARIOS (Grupos VARCHAR (50) NOT NULL DEFAULT "...", Usuarios VARCHAR (20) NOT NULL DEFAULT "...", PRIMARY KEY (Grupos, Usuarios));
INSERT INTO GRUPO_USUARIOS (Grupos, Usuarios) VALUES ('futbol', 'mateoiba');
INSERT INTO GRUPO_USUARIOS (Grupos, Usuarios) VALUES ('Amigos', 'pedritoVM');
INSERT INTO GRUPO_USUARIOS (Grupos, Usuarios) VALUES ('Escuela', 'elena30');
INSERT INTO GRUPO_USUARIOS (Grupos, Usuarios) VALUES ('futbol', 'alejandro123');

-- Table: RELACION
CREATE TABLE RELACION (Origen VARCHAR (50) NOT NULL REFERENCES USUARIOS (Usuario) ON DELETE CASCADE ON UPDATE CASCADE MATCH SIMPLE DEFAULT "...", Destino VARCHAR (50) NOT NULL DEFAULT Publico, Tipo VARCHAR (1) NOT NULL REFERENCES TIPO ("ID tipo") ON DELETE CASCADE ON UPDATE CASCADE MATCH "FULL" DEFAULT P, Fecha VARCHAR (8) NOT NULL DEFAULT "00000000", Hora VARCHAR (12) NOT NULL DEFAULT "00:00:00.000", Texto VARCHAR (250) NOT NULL DEFAULT "...");
INSERT INTO RELACION (Origen, Destino, Tipo, Fecha, Hora, Texto) VALUES ('elena30', 'susana34', 'U', '20211212', '10:12:12.123', 'a ver si anda...');
INSERT INTO RELACION (Origen, Destino, Tipo, Fecha, Hora, Texto) VALUES ('mateoiba', 'futbol', 'G', '20200827', '17:54:34.228', 'Eu rspondann');
INSERT INTO RELACION (Origen, Destino, Tipo, Fecha, Hora, Texto) VALUES ('mateoiba', 'Amigos', 'G', '20200827', '17:45:12.989', 'Quien se prende en un futbol???');
INSERT INTO RELACION (Origen, Destino, Tipo, Fecha, Hora, Texto) VALUES ('pedritoVM', 'alejandro123', 'U', '20210609', '19:41:21.322', 'no flaco, hacelo vos...');
INSERT INTO RELACION (Origen, Destino, Tipo, Fecha, Hora, Texto) VALUES ('alejandro123', 'pedritoVM', 'U', '20210609', '19:35:56.274', 'me pasas el tp de matemática?');
INSERT INTO RELACION (Origen, Destino, Tipo, Fecha, Hora, Texto) VALUES ('robertooh', 'Publico', 'P', '20190101', '00:01:12.456', '¡Feliz año nuevo a todos!!!');
INSERT INTO RELACION (Origen, Destino, Tipo, Fecha, Hora, Texto) VALUES ('elena30', 'Escuela', 'G', '19991212', '12:12:12.120', 'cuando empiezan las clases???');
INSERT INTO RELACION (Origen, Destino, Tipo, Fecha, Hora, Texto) VALUES ('mateoiba', 'Amigos', 'G', '20210705', '07:34:12.735', 'Hola ¿todo bien?');
INSERT INTO RELACION (Origen, Destino, Tipo, Fecha, Hora, Texto) VALUES ('susana34', 'Publico', 'P', '19991212', '12:59.55.754', 'este me imagino que es el ultimo mensajito que se envia en el mileño');
INSERT INTO RELACION (Origen, Destino, Tipo, Fecha, Hora, Texto) VALUES ('susana34', 'mateoiba', 'U', '19981231', '11:54:23.765', 'En un año y 1 minuto vamos a estar en otro mileño');
INSERT INTO RELACION (Origen, Destino, Tipo, Fecha, Hora, Texto) VALUES ('robertooh', 'Publico', 'P', '20201223', '12.02.23.128', 'alguien sabe como calcular un promedio? DIGANME SI SABENN');
INSERT INTO RELACION (Origen, Destino, Tipo, Fecha, Hora, Texto) VALUES ('pedritoVM', 'Escuela', 'G', '20210930', '19:42:24.123', 'hay tarea para mañana???');
INSERT INTO RELACION (Origen, Destino, Tipo, Fecha, Hora, Texto) VALUES ('elena30', 'robertooh', 'U', '20190223', '23:23:23.230', 'Estoy aburridaa');
INSERT INTO RELACION (Origen, Destino, Tipo, Fecha, Hora, Texto) VALUES ('alejandro123', 'Publico', 'P', '20210608', '19:40:58:12.212', 'Denle like a mi ultima publicacion');
INSERT INTO RELACION (Origen, Destino, Tipo, Fecha, Hora, Texto) VALUES ('alejandro123', 'Amigos', 'G', '20210807', '16:54:59.845', 'a alguien le sobra un auto ue e pueda prestar?');
INSERT INTO RELACION (Origen, Destino, Tipo, Fecha, Hora, Texto) VALUES ('mateoiba', 'alejandro123', 'U', '20210808', '12:23:17.371', 'yo tengo un auto ale, pero que el resto no se entere');
INSERT INTO RELACION (Origen, Destino, Tipo, Fecha, Hora, Texto) VALUES ('susana34', 'mateoiba', 'U', '20211117', '15:34:56.345', 'compra facturitas cuando vengas');
INSERT INTO RELACION (Origen, Destino, Tipo, Fecha, Hora, Texto) VALUES ('pedritoVM', 'susana34', 'U', '19990609', '19:10:12.100', 'alguna serie para recomendar en netflix?');
INSERT INTO RELACION (Origen, Destino, Tipo, Fecha, Hora, Texto) VALUES ('elena30', 'pedritoVM', 'U', '20191254', '12:38:21.099', 'compra bitcoins pedrito');
INSERT INTO RELACION (Origen, Destino, Tipo, Fecha, Hora, Texto) VALUES ('elena30', 'Publico', 'P', '20191254', '1235:43.434', 'no compren bitcoins, sn una estafa');

-- Table: TIPO
CREATE TABLE TIPO ("ID tipo" VARCHAR (1) NOT NULL PRIMARY KEY DEFAULT P, "nombre tipo" VARCHAR (30) NOT NULL DEFAULT Publico);
INSERT INTO TIPO ("ID tipo", "nombre tipo") VALUES ('U', 'privado');
INSERT INTO TIPO ("ID tipo", "nombre tipo") VALUES ('G', 'grupal');
INSERT INTO TIPO ("ID tipo", "nombre tipo") VALUES ('P', 'público');

-- Table: USUARIOS
CREATE TABLE USUARIOS (Usuario VARCHAR (50) NOT NULL PRIMARY KEY DEFAULT "...", clave VARCHAR (10) NOT NULL DEFAULT (123));
INSERT INTO USUARIOS (Usuario, clave) VALUES ('susana34', '456');
INSERT INTO USUARIOS (Usuario, clave) VALUES ('mateoiba', '2572000000');
INSERT INTO USUARIOS (Usuario, clave) VALUES ('elena30', '1223355');
INSERT INTO USUARIOS (Usuario, clave) VALUES ('pedritoVM', '4444555');
INSERT INTO USUARIOS (Usuario, clave) VALUES ('robertooh', '420069');
INSERT INTO USUARIOS (Usuario, clave) VALUES ('alejandro123', '123');

-- View: TP 8 3.1
CREATE VIEW "TP 8 3.1" AS SELECT RELACION.Origen, RELACION.Destino, RELACION.Fecha, RELACION.Hora, RELACION.Texto
FROM RELACION

ORDER BY RELACION.Fecha DESC, RELACION.Hora DESC;

-- View: TP 8 3.2
CREATE VIEW "TP 8 3.2" AS SELECT RELACION.Origen AS 'Usuario', RELACION.Destino AS 'Grupo', count(RELACION.Destino) AS 'Cantidad de Mensajes'
FROM RELACION

WHERE RELACION.Tipo=="G" AND RELACION.Origen=="mateoiba"

GROUP BY RELACION.Destino
ORDER BY 'Cantided de Mensajes';

-- View: TP8 3.3
CREATE VIEW "TP8 3.3" AS SELECT RELACION.Fecha, COUNT(RELACION.Texto) AS 'Cantidad_de_Mensajes'
FROM RELACION

GROUP BY RELACION.Fecha
ORDER BY RELACION.Fecha DESC;

-- View: TP8 3.4
CREATE VIEW "TP8 3.4" AS SELECT td.Origen, max(td.Cantidad_de_Mensajes) as 'Cantidad de Mensajes'
FROM
(SELECT RELACION.Origen, COUNT(RELACION.Texto) AS 'Cantidad_de_Mensajes'
FROM RELACION

GROUP BY RELACION.Origen) as 'td';

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
