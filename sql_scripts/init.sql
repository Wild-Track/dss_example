-- #region Creation of db structure
-- Create database
CREATE DATABASE IF NOT EXISTS insurance_example CHARACTER
SET
  utf8mb4 COLLATE utf8mb4_unicode_ci;

USE insurance_example;

CREATE TABLE
  agencies_revenues (
    `agency_id` INT NOT NULL,
    `year_month` TIMESTAMP NOT NULL,
    `total_income` FLOAT NOT NULL,
    `expenses` FLOAT NOT NULL,
    PRIMARY KEY (`agency_id`, `year_month`)
  );

CREATE TABLE
  travels (
    `id` INT NOT NULL AUTO_INCREMENT,
    `agency_id` INT NOT NULL,
    `product_id` INT NOT NULL,
    `claim` VARCHAR(255) NOT NULL,
    `country_id_of_destination` INT NOT NULL,
    `net_sales` FLOAT NOT NULL,
    `commission` FLOAT NOT NULL,
    `age` INT NOT NULL,
    `date` TIMESTAMP NOT NULL,
    PRIMARY KEY (`id`)
  );

CREATE TABLE
  agencies (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `type_id` INT NOT NULL,
    PRIMARY KEY (`id`)
  );

CREATE TABLE
  products (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `category_id` INT NOT NULL,
    PRIMARY KEY (`id`)
  );

CREATE TABLE
  categories (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
  );

CREATE TABLE
  agencies_types (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `agencies_types_name` (`name`)
  );

CREATE TABLE
  countries (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    PRIMARY KEY (`id`)
  );

ALTER TABLE `agencies` ADD CONSTRAINT id_type_id FOREIGN KEY (`type_id`) REFERENCES `agencies_types` (`id`);

ALTER TABLE `agencies_revenues` ADD CONSTRAINT id_agency_id_agencies_revenues FOREIGN KEY (`agency_id`) REFERENCES `agencies` (`id`);

ALTER TABLE `travels` ADD CONSTRAINT id_agency_id_travels FOREIGN KEY (`agency_id`) REFERENCES `agencies` (`id`);

ALTER TABLE `travels` ADD CONSTRAINT id_destination FOREIGN KEY (`country_id_of_destination`) REFERENCES countries (`id`);

ALTER TABLE `products` ADD CONSTRAINT id_category_id FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`);

ALTER TABLE `travels` ADD CONSTRAINT `id_product_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`);