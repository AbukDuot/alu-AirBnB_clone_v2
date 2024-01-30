--the existance of the database is checked before creating it
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
--the existance of the user is checked before creating it
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
--privileges are granted to the user
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema . * TO 'hbnb_dev'@'localhost';
