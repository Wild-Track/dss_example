-- #region Creation of db structure
-- Create database
CREATE DATABASE IF NOT EXISTS si CHARACTER
SET
  utf8mb4 COLLATE utf8mb4_unicode_ci;

USE si;

-- Create clients table
CREATE TABLE
  clients (
    `id` INT NOT NULL,
    `country` VARCHAR(64) NOT NULL,
    PRIMARY KEY (id)
  ) CHARACTER
SET
  utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Create products table
CREATE TABLE
  products (
    `id` INT NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    `main_category` VARCHAR(255) NOT NULL,
    `sub_category` VARCHAR(255) NOT NULL,
    `image` VARCHAR(255) NOT NULL,
    `link` VARCHAR(255) NOT NULL,
    `rating` FLOAT,
    `nb_rating` INT,
    `discount_price` FLOAT,
    `actual_price` FLOAT,
    PRIMARY KEY (id)
  ) CHARACTER
SET
  utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Create sales table
CREATE TABLE
  sales (
    `id` INT NOT NULL,
    `date` DATETIME NOT NULL,
    `is_discount` BOOLEAN NOT NULL,
    `clients_id` INT NOT NULL,
    PRIMARY KEY (id)
  ) CHARACTER
SET
  utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Create product_details table
CREATE TABLE
  product_details (
    `sales_id` INT NOT NULL,
    `products_id` INT NOT NULL,
    `quantity` INT NOT NULL,
    PRIMARY KEY (`sales_id`, `products_id`)
  ) CHARACTER
SET
  utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Add foreign key
ALTER TABLE sales ADD CONSTRAINT clients_sales FOREIGN KEY (`clients_id`) REFERENCES clients (`id`);

ALTER TABLE product_details ADD CONSTRAINT sales_product_details FOREIGN KEY (`sales_id`) REFERENCES sales (`id`);

ALTER TABLE product_details ADD CONSTRAINT products_product_details FOREIGN KEY (`products_id`) REFERENCES products (`id`);

-- #endregion Creation of db structure