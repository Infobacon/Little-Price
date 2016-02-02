-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 02-02-2016 a las 07:40:49
-- Versión del servidor: 5.6.21
-- Versión de PHP: 5.6.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `little_price`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `insertarCategoria`(
IN _nombre varchar(100),
IN _desc varchar(100) )
BEGIN

INSERT INTO categoria (nombre,descripcion) VALUES (_nombre,_desc);

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `insertarProducto`(
IN _id_categoria INT,
IN _nombre varchar(100),
IN _marca varchar(100),
IN _desc varchar(100),
IN _cantidad FLOAT )
BEGIN

INSERT INTO producto (id_categoria,nombre,marca,descripcion,cantidad) VALUES (_id_categoria,_nombre,_marca,_desc,_cantidad);

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `insertarProductoPrecio`(
IN _id_supermercado INT,
IN _id_producto INT,
IN _id_usuario INT,
IN _precio INT )
BEGIN

INSERT INTO producto_precio (id_supermercado,id_producto,id_usuario,precio,fecha,cant_valoracionpos,cant_valoracionneg,estado_confirmacion)
VALUES (_id_supermercado,_id_producto,_id_usuario,_precio,CURRENT_DATE,0,0,0);

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `insertarReporte`(
IN _id_usuario INT,
IN _id_producto_precio INT,
IN _comentario varchar(1024) )
BEGIN

INSERT INTO reporte (id_usuario,id_producto_precio,fecha,COMENTARIO) VALUES (_id_usuario,_id_producto_precio,CURRENT_DATE,_comentario);

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `insertarSupermercado`(
IN _nombre varchar(100),
IN _direccion varchar(100),
IN _lat decimal(9,6),
IN _lon decimal(9,6) )
BEGIN

INSERT INTO supermercado (nombre,direccion,latitud,longitud) VALUES (_nombre,_direccion,_lat,_lon);

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `insertarUsuario`(
IN _nombre varchar(50),
IN _correo varchar(50),
IN _contrasena varchar(30) )
BEGIN

DECLARE username_dup INT;
DECLARE email_dup INT;

SELECT COUNT(*) INTO username_dup FROM usuario where usuario.NOMBRE_USUARIO= _nombre;
SELECT COUNT(*) INTO email_dup FROM usuario where usuario.CORREO= _correo;

IF username_dup = 0 AND email_dup = 0 THEN

INSERT INTO usuario (NOMBRE_USUARIO,correo,contrasena,CANT_REPORTES,ESTADO_CUENTA,PORCENTAJE_CONFIABILIDAD) VALUES (_nombre,_correo,_contrasena,0,0,0);


END IF;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `insertarValoracion`(
IN _id_usuario INT,
IN _id_producto_precio INT,
IN _valoracion INT )
BEGIN

INSERT INTO valoracion (id_usuario,id_producto_precio,valoracion,fecha) VALUES (_id_usuario,_id_producto_precio,_valoracion,CURRENT_DATE);

END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
`id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `name` (`name`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
