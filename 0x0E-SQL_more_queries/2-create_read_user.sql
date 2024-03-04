-- A Script that creates the database hbtn_0d_2 and user user_od_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
FLUSH PRIVILEGES;
