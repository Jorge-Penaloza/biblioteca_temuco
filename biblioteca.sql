-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-10-2021 a las 03:11:17
-- Versión del servidor: 10.4.21-MariaDB
-- Versión de PHP: 7.4.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `biblioteca`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `colaboracion`
--

CREATE TABLE `colaboracion` (
  `codigo` varchar(20) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `colaboracion`
--

INSERT INTO `colaboracion` (`codigo`, `nombre`) VALUES
('1', 'Interno'),
('2', 'IACC'),
('3', 'AIEP'),
('4', 'Duoc');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libros`
--

CREATE TABLE `libros` (
  `codigo` varchar(20) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `autor` varchar(50) DEFAULT NULL,
  `descripcion` varchar(250) DEFAULT NULL,
  `anio` int(4) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `libros`
--

INSERT INTO `libros` (`codigo`, `nombre`, `autor`, `descripcion`, `anio`, `cantidad`) VALUES
('A10', 'El capital', 'Karl Marx', 'Crítica de la economía política es un texto teórico fundamental en la filosofía, economía y política de Karl Marx', 1970, 10),
('A20', 'La ética de la libertad', 'Murray Rothbard', 'La ética de la libertad, escrito por el economista e historiador Murray N. Rothbard, publicado por primera vez en 1982, es una exposición lógica y ética sobre la posición política del anarcocapitalismo', 1982, 12);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prestamo`
--

CREATE TABLE `prestamo` (
  `id` int(11) NOT NULL,
  `prestamo` int(11) NOT NULL,
  `fecha` date DEFAULT NULL,
  `horario` time DEFAULT NULL,
  `usuario` varchar(50) DEFAULT NULL,
  `codigolibro` varchar(20) DEFAULT NULL,
  `codigocolaboracion` varchar(20) DEFAULT NULL,
  `estado` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `prestamo`
--

INSERT INTO `prestamo` (`id`, `prestamo`, `fecha`, `horario`, `usuario`, `codigolibro`, `codigocolaboracion`, `estado`) VALUES
(3, 1, '2021-10-17', '22:07:18', '2', 'A20', '1: Interno', 'En préstamo'),
(4, 2, '2021-10-17', '22:07:55', '13834570-k', 'A20', '2: IACC', 'En préstamo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `usuario` varchar(50) NOT NULL,
  `clave` varchar(50) NOT NULL,
  `perfil` char(1) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `usuario`, `clave`, `perfil`, `nombre`) VALUES
(1, '1', '356a192b7913b04c54574d18c28d46e6395428ab', 'A', 'Jorge Peñaloza'),
(2, '2', 'da4b9237bacccdf19c0760cab7aec4a8359010b0', 'U', 'Ricardo');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `colaboracion`
--
ALTER TABLE `colaboracion`
  ADD PRIMARY KEY (`codigo`);

--
-- Indices de la tabla `libros`
--
ALTER TABLE `libros`
  ADD PRIMARY KEY (`codigo`);

--
-- Indices de la tabla `prestamo`
--
ALTER TABLE `prestamo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `codigobook_idx` (`codigolibro`),
  ADD KEY `codigocolab_idx` (`codigocolaboracion`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`,`usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `prestamo`
--
ALTER TABLE `prestamo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
