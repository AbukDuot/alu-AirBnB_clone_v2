--the existance of the database is checked before creating it
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `hbnb_dev_db`;

--the existance of the user is checked before creating it
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
--privileges are granted to the user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';


GRANT SELECT, INSERT, UPDATE, DELETE ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

