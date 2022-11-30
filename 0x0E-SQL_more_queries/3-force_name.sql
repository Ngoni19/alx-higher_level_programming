-- script creates the table force_name on MySQL server
-- data insert into table: id INT, name VARCHAR(256) can’t be null
-- database name will be passed as an argument of the mysql command
-- if table exists, script should not fail

CREATE TABLE IF NOT EXISTS force_name (
       id INT,
       name VARCHAR(256) NOT NULL
);
