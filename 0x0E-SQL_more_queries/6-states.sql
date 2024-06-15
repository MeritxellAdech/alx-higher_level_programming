-- Creating a table within a database

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- selecting that database to ensure the table is created in it
USE hbtn_0d_usa;

-- Creating the table
CREATE TABLE IF NOT EXISTS states
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
