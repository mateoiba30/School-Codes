--
-- File generated with SQLiteStudio v3.0.7 on mar. mar. 30 18:41:48 2021
--
-- Text encoding used: windows-1252
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Participantes
CREATE TABLE Participantes (ID INT (2) PRIMARY KEY NOT NULL, Apellido VARCHAR (50) NOT NULL, Nombre VARCHAR (50) NOT NULL, Localidad VARCHAR (50) NOT NULL, Provincia VARCHAR (50), País VARCHAR (50) NOT NULL);
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (30, 'Bangher', 'Debora Natalia', 'Resistencia', NULL, '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (31, 'Barrera', 'Corina Anahí', 'Córdoba', 'Córdoba', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (32, 'Barriga', 'Lucía Guadalupe', 'San Martín', 'Buenos Aires', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (33, 'Barrionuevo', 'Cristian Gustavo', 'Comodoro Rivadavia', 'Chubut', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (35, 'Battaglia', 'María José', 'Maipú', 'Mendoza', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (29, 'Balbuena', 'María Sol', 'Buenos Aires', 'Ciudad Autónoma de Buenos Aires', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (20, 'Argüelllo Caro', 'Evangelina Beatriz', 'Córdoba', 'Córdoba', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (21, 'Aramni', 'Paula', 'Trelew', 'Chubut', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (22, 'Armúa de Reyes', 'Aurora Cristina', 'Corrientes', 'Corrientes', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (23, 'Avila', 'Gerardo Sergio', 'San Carlos de Bariloche', 'Río Negro', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (24, 'Ávila', 'Ana Lucía', 'San Miguel de Tucumán', 'Tucumán', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (25, 'Ayala', 'Mahia Mariel', 'Posadas', 'Misiones', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (26, 'Ayón', 'Rosana', 'Capital', 'Salta', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (27, 'Bachmann', 'Guillermo Enrique', 'Muñiz(San Miguel)', 'Buenos Aires', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (28, 'Bado', 'Silvina Graciela', 'Trelew', 'Chubut', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (12, 'Alzogaray', 'Raúl Adolfo', 'Buenos Aires', 'Ciudad Autónoma de Buenos Aires', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (13, 'Andrade Rojas', 'María Paola', 'Santiago', 'Santiago', '2');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (14, 'Angulo Lewylle', 'Maricel', 'Castelar', 'Buenos Aires', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (15, 'Aquino', 'Daniel', 'La Plata', 'Bs Aires', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (16, 'Aranda', 'Susana Graciela', 'San Miguel de Tucumán', 'Tucumán', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (17, 'Arbetman', 'Martina', 'Bariloche', 'R. Negro', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (18, 'Archangelsky', 'Miguel', 'Esquel', '', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (19, 'Thomsett Herbert', 'Lucía', 'Gral. San Martín', 'Buenos Aires', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (3, 'Acardi', 'Soraya Alejandra', 'Posadas', 'Misiones', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (4, 'Acuña', 'Lucía Raily', 'Posadas', 'Misiones', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (6, 'Aguirre', 'María Belen', 'Capital Federal', 'Ciudad Autónoma de Ciudad Autónoma de Buenos Aires', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (7, 'Aisen', 'Santiago', 'an Carlos de Bariloche', 'Río Negro', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (8, 'Albicocco', 'Andrea Paola', 'Ciudad Autónoma de Ciudad Autónoma de Buenos Aires', 'Ciudad Autónoma de Ciudad Autónoma de Buenos Aires', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (9, 'Almirón', 'Walter Ricardo', 'Córdoba', 'Córdoba', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (11, 'Alvarez Costa', 'Agustín', 'Adrogué', 'Bs As', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (2, 'Abraham', 'Solana', 'San Miguel de Tucumán', 'Tucumán', '1');
INSERT INTO Participantes (ID, Apellido, Nombre, Localidad, Provincia, País) VALUES (1, 'Aballay', 'Fernando', 'Godoy Cruz', 'Mendoza', '1');

-- Table: IDdePaíses
CREATE TABLE IDdePaíses ("ID.país" INT (1) NOT NULL, País VARCHAR (25) NOT NULL);
INSERT INTO IDdePaíses ("ID.país", País) VALUES (1, 'Argentina');
INSERT INTO IDdePaíses ("ID.país", País) VALUES (1, 'Arg');
INSERT INTO IDdePaíses ("ID.país", País) VALUES (1, 'ARG');
INSERT INTO IDdePaíses ("ID.país", País) VALUES (1, 'ARGENT');
INSERT INTO IDdePaíses ("ID.país", País) VALUES (1, 'República Argentina');
INSERT INTO IDdePaíses ("ID.país", País) VALUES (2, 'CHILE');

-- View: act 3.2.
CREATE VIEW "act 3.2." AS SELECT Apellido, Nombre FROM Participantes

WHERE (País=1)

ORDER BY Apellido, Nombre;

-- View: act 3.1.
CREATE VIEW "act 3.1." AS SELECT Apellido, Nombre FROM Participantes

ORDER BY Apellido, Nombre;

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
