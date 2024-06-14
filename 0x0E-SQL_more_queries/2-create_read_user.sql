-- Creating the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Creating a user
CREATE USER IF NOT EXISTS "user_0d_2"@"localhost" IDENTIFIED BY 'user_0d_2_pwd';

-- Granting user_0d_2 SELECT permission on hbtn_0d_2 
GRANT SELECT ON hbtn_0d_2.* TO 'hbtn_0d_2'@'localhost';