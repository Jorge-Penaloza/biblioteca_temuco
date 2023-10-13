-- MySQL Workbench Synchronization
-- Generated: 2021-10-11 23:42
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: ricar

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

ALTER SCHEMA `biblioteca`  DEFAULT CHARACTER SET utf8  DEFAULT COLLATE utf8_general_ci ;

CREATE TABLE IF NOT EXISTS `biblioteca`.`usuarios` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `usuario` VARCHAR(50) NOT NULL,
  `clave` VARCHAR(50) NOT NULL,
  `perfil` CHAR(1) NOT NULL,
  `nombre` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`, `usuario`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `biblioteca`.`colaboracion` (
  `codigo` VARCHAR(20) NOT NULL,
  `nombre` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`codigo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `biblioteca`.`libros` (
  `codigo` VARCHAR(20) NOT NULL,
  `autor` VARCHAR(50) NULL DEFAULT NULL,
  `descripcion` VARCHAR(50) NULL DEFAULT NULL,
  `anio` INT(4) NULL DEFAULT NULL,
  `cantidad` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`codigo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

-- MySQL Workbench Synchronization
-- Generated: 2021-10-11 23:56
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: ricar

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE TABLE IF NOT EXISTS `biblioteca`.`prestamo` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `fecha` DATE NULL DEFAULT NULL,
  `horario` TIME NULL DEFAULT NULL,
  `usuario` VARCHAR(50) NULL DEFAULT NULL,
  `codigolibro` VARCHAR(20) NULL DEFAULT NULL,
  `codigocolaboracion` VARCHAR(20) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `codigobook_idx` (`codigolibro` ASC),
  INDEX `codigocolab_idx` (`codigocolaboracion` ASC),
  CONSTRAINT `codigobook`
    FOREIGN KEY (`codigolibro`)
    REFERENCES `biblioteca`.`libros` (`codigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `codigocolab`
    FOREIGN KEY (`codigocolaboracion`)
    REFERENCES `biblioteca`.`colaboracion` (`codigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;




