-- Creating a table with 1 as ID default value and unique
CREATE TABLE IF NOT EXISTS unique_id
(
    id INT DEFAULT(1) UNIQUE,
    name VARCHAR(256)
);