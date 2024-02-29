-- A script that creates a table second_table.
CREATE TABLE IF NOT EXISTS second_table(
    id INTEGER,
    name VARCHAR(256),
    score INTEGER);
INSERT INTO second_table (id, name, score)
VALUES
(1, "John", 10),
(2, "ALEX", 3),
(3, "Bob", 14),
(4, "George", 8);
