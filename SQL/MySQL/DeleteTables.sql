-- BORRAR TABLAS

-- SELECCIONAR BASE DE DATOS
USE USUARIOS;

SET NAMES utf8mb4;

-- VER VARIABLE GLOBAL
SHOW VARIABLES LIKE "SQL_SAFE_UPDATES";
-- DESHABILITAR ACTUALIZACION SEGURA
SET SQL_SAFE_UPDATES = 0;

-- TABLE DELETE
DELETE FROM tasks_task;
-- SELECCIONAR TABLA
SELECT * FROM tasks_task;

-- TABLE DELETE
DELETE FROM auth_user;
-- SELECCIONAR TABLA
SELECT * FROM auth_user;

-- HABILITAR ACTUALIZACION SEGURA
SET SQL_SAFE_UPDATES = 1;
-- VER VARIABLE GLOBAL
SHOW VARIABLES LIKE "SQL_SAFE_UPDATES";