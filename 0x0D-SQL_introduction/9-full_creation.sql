-- A script that creates a table second_table.
DROP TABLE IF EXISTS second_table;
CREATE TABLE second_table(
    id INTEGER,
    name VARCHAR(256),
    score INTEGER);
INSERT INTO second_table
VALUES
(1, "John", 10),
(2, "ALEX", 3),
(3, "Bob", 14),
(4, "George", 8);
