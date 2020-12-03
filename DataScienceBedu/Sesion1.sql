/*Este es un re-view para estudiar la sesión 1 del curso Data Analysis de BEDU x Santander*/
SHOW DATABASES; #Muestra las bases de datos disponibles, ojo no utilizar 'information_schema'
USE tienda; #Selecciona una base de datos
SHOW TABLES; #Muestra todas las tablas y tambien las listas
DESCRIBE empleado;/* Nos muestra la descrioción completa de la tabla,
					Incluye el tipo de dato, si puede ser nulo o no, si es llave
                    primaria o no, valor por defecto y consideraciones extas*/

/* CONSULTAS BÁSICAS */
SELECT nombre FROM empleado;
/*Se agregan los atributos que queremos saber, si es más de uno, se separan por comas, 
   si queremos todos los datos usamos *,posterior se dice de donde se obtendra ese dato*/
SELECT * FROM empleado;
/* Para colocar una restricción, utilizamos WHERE, se debe de colocar el atributo y un valor especifico */
SELECT id_empleado,nombre FROM empleado WHERE id_empleado < 100; #Regresa la lista en orden ASC
/* Se pueden utilizar tambien operadores logicos, AND, OR, NOT */
SELECT id_empleado,nombre FROM empleado WHERE id_empleado >= 200 AND id_empleado <=252;
SELECT id_empleado,nombre FROM empleado WHERE id_empleado = 200 OR id_empleado = 252;
#Otra forma de utilizar OR es con el operador IN, donde se colocara una lista de posibles valores
SELECT id_empleado,nombre FROM empleado WHERE id_empleado IN (10,100,110);

/* Ordenamientos y Limites */
SELECT * FROM puesto ORDER BY salario DESC; #Ejemplo del ranking de quien gana más
SELECT clave,fecha FROM venta ORDER BY fecha DESC; #Las ultimas ventas que se han hecho
SELECT nombre,cantidad FROM articulo ORDER BY cantidad ASC; #Ordena los articulos del que haya menos al que haya más 
SELECT nombre,cantidad FROM articulo ORDER BY cantidad; #Hace lo mismo que la de arribla, el ASC no es necesario, esta por default
SELECT * FROM puesto ORDER BY salario LIMIT 5; #Los 5 que ganan menos
SELECT * FROM puesto ORDER BY salario DESC LIMIT 5; #Los 5 que ganan más 

/* Retos */
#1
#La respuesta al reto 1 esta en la imagen del respositorio con el nombre 'sesión1_reto1'
#2
