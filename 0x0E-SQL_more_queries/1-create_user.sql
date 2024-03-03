-- Check if the user exists and drop if it exists.
DROP USER IF EXISTS user_0d_1@localhost;
-- Create the MYSQL user user_0d_1
CREATE USER 'user_0d_1'@localhost IDENTIFIED BY 'user_0d_1_pwd';
-- Grant all privileges to the user
GRANT ALL ON *.* TO user_0d_1@localhost;
