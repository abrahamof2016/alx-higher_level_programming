/* A Script that creates the database hbtn_0d_2 and user user_od_2 */
DROP USER IF EXISTS 'user_0d_2'@'localhost';
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
DROP DATABASE IF EXISTS hbtn_0d_2;
CREATE DATABASE hbtn_0d_2;
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
FLUSH PRIVILEGES;
