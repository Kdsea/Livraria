CREATE DATABASE librabrydb;

CREATE TABLE `librabrydb`.`user` (
  `iduser` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(60) NOT NULL,
  `data_nascimento` DATE NOT NULL,
  `endereco` VARCHAR(100) NOT NULL,
  `telefone` VARCHAR(14) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`iduser`))

CREATE TABLE IF NOT EXISTS `librabrydb`.`livro` (
  `idlivros` INT NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `editora` VARCHAR(45) NOT NULL,
  `autor` VARCHAR(45) NOT NULL,
  `data_inserida` DATE NOT NULL,
  `alugado` TINYINT NOT NULL,
  PRIMARY KEY (`idlivros`))

CREATE TABLE IF NOT EXISTS `librabrydb`.`livro_has_user` (
  `livro_idlivros` INT NOT NULL,
  `user_iduser` INT NOT NULL,
  PRIMARY KEY (`livro_idlivros`, `user_iduser`),
  INDEX `fk_livro_has_user_user1_idx` (`user_iduser` ASC) VISIBLE,
  INDEX `fk_livro_has_user_livro_idx` (`livro_idlivros` ASC) VISIBLE,
  CONSTRAINT `fk_livro_has_user_livro`
    FOREIGN KEY (`livro_idlivros`)
    REFERENCES `mydb`.`livro` (`idlivros`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_livro_has_user_user1`
    FOREIGN KEY (`user_iduser`)
    REFERENCES `mydb`.`user` (`iduser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB