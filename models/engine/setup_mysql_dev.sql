CREATE DATABASE IF NOT EXISTS `hbnb_dev_db` /*!40100 DEFAULT CHARACTER SET utf8 */;


CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

GRANT SELECT, INSERT, UPDATE, DELETE ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

