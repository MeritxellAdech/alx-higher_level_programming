-- Creating the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Creating a user
CREATE USER IF NOT EXISTS "user_0d_2"@"localhost" IDENTIFIED BY 'user_0d_2_pwd';

-- Ensuring that the user account is valid
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';

-- Granting user_0d_2 SELECT permission on hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';