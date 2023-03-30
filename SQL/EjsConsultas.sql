
/*-- Ej 1 
SELECT 5+10, 10-5, 10*5, 10/5;
-- Ej 2
SELECT 5+10 AS suma, 10-5 AS resta, 10*5 AS producto, 10/5 AS cociente;
-- Ej 3 
SELECT nombre, apellido1, apellido2 FROM asistente WHERE empresa='BK Programación';
-- EJ 4
SELECT nombre, capacidad FROM sala
ORDER BY capacidad DESC;
-- Ej 5
SELECT * FROM asistente WHERE empresa = 'Bigsoft'
ORDER BY fechaNac DESC;
-- Ej 6
SELECT COUNT(codigo) AS 'Asistentes', empresa FROM asistente 
WHERE empresa IS NOT NULL
GROUP BY empresa ;
-- Ej 7 
SELECT nombre, apellido1, apellido2 FROM asistente
ORDER BY apellido1 ASC 
LIMIT 0, 5;
-- Ej 8 
SELECT tema, fecha FROM conferencia
WHERE turno='T'
AND sala IN ('Apolo', 'Zeus');
-- Ej 9 
SELECT * FROM asistente
WHERE apellido1 LIKE 'M%r%';
-- Ej 10
SELECT * FROM conferencia
WHERE precio>12 AND precio<19
AND tema NOT IN ('Programación web');
-- Ej 11 
SELECT CONCAT(apellido1, if(apellido2 IS NULL, "", concat(" ", apellido2))) 
AS Apellidos, 
fechaNac, empresa 
FROM asistente 
WHERE fechaNac BETWEEN '1974-01-01' AND '1985-01-01' 
ORDER BY fechaNac;
-- Ej 12 
SELECT * FROM conferencia
WHERE tema LIKE 'Programacion%'
ORDER BY precio DESC;
-- Ej 13
SELECT tema,
precio AS 'Sin descuento',
precio * (1 - .05) AS '5% descuento',
precio * (1 - .1) AS '10% descuento',
precio * (1 - .15) AS '15% descuento',
precio * (1 - .2) AS '20% descuento'
FROM conferencia;
-- Ej 14
 SELECT tema, 
 round(precio * 0.95) AS 'precio final',
 DATE_FORMAT(fecha, '%d/%m/%Y') AS fecha
 FROM conferencia
 ORDER BY 'precio final' desc;
 -- Ej 15
 SELECT 
 UPPER(nombre) AS 'Nombre',
 UPPER(if(apellido2 is not NULL, CONCAT(apellido1," ",apellido2), apellido1)) AS 'Apellido Resultante',
 UPPER(especialidad) AS 'Especialidad'
 FROM ponente
 ORDER BY 'Apellido Resultante' ASC;
 -- Ej 16 
 SELECT 
 UPPER(nombre) AS 'Nombre',
 UPPER(if(apellido2 is not NULL, CONCAT(apellido1," ",apellido2), concat(apellido1, ' *****'))) AS 'Apellido Resultante',
 UPPER(especialidad) AS 'Especialidad'
 FROM ponente
  ORDER BY 'Apellido Resultante' ASC;
 -- Ej 17 
 
 SELECT 
 UPPER( RPAD(nombre, 10, '*') ) AS 'Nombre',
 UPPER(if(apellido2 is not NULL, CONCAT(apellido1," ",apellido2), concat(apellido1, ' *****'))) AS 'Apellido Resultante',
 UPPER(especialidad) AS 'Especialidad'
 FROM ponente
ORDER BY 'Apellido Resultante' ASC;

-- Ej 18
SELECT 
if(nombre not IN('Jose'),nombre, 'Pepe') AS 'Nombre',
apellido1 AS 'PrimerApellido',
if(apellido2 is not NULL, apellido2, '') AS 'SegundoApellido', 
LENGTH(CONCAT(nombre, apellido1, if(apellido2 is not NULL, apellido2, ''))) AS 'Longitud'
FROM asistente;
-- Ej 19 */
select nombre,
if(apellido2 is null, apellido1, concat(apellido1," ", apellido2)) as 'Apellidos',
DATEDIFF(NOW(), fechaNac) AS 'Días vividos'
from asistente