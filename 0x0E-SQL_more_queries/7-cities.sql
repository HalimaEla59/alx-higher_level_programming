-- creates the database hbtn_0d_usa and the table cities in it
-- id INT unique, auto generated, can’t be null and is a primary key
-- state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
-- name VARCHAR(256) can’t be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities
(`id` INT NOT NULL AUTO_INCREMENT, UNIQUE(`id`), PRIMARY KEY(`id`),`state_id` INT NOT NULL, FOREIGN KEY(`state_id`) REFERENCES states(`id`), `name` VARCHAR(256) NOT NULL);
