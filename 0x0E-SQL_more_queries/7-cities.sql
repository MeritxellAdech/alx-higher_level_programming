-- Creating a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- using hbtn_0d_usa as database
USE hbtn_0d_usa;

-- creating a table
CREATE TABLE IF NOT EXISTS cities
(
    id INT AUTO_INCREMENT PRIMARY KEY UNIQUE,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    CONSTRAINT fk_states_id FOREIGN KEY (state_id) REFERENCES states(id)
);