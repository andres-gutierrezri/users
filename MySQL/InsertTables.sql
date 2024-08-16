-- INSERTAR LIBROS

-- SELECCIONAR BASE DE DATOS
USE CRUD_django;

SET NAMES utf8;

-- SELECCIONAR TABLA
SELECT * FROM tasks_factura ORDER BY numero_factura asc;

-- REINICIAR INCREMENTO
ALTER TABLE tasks_factura AUTO_INCREMENT = 1;

-- INSERTAR VALORES
INSERT INTO
    tasks_factura (
        numero_factura,
        nombre,
        direccion,
        telefono,
        fecha_nacimineto,
        genero,
        user_id
    )
VALUES (
        1,
        'julio',
        'calle 45',
        '12345787',
        '2000-12-12',
        'm',
        1
    );

-- SELECCIONAR TABLA
SELECT * FROM tasks_factura;