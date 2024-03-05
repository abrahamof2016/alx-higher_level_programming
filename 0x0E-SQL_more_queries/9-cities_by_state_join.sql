-- A script taht lists all cities contained in the database hbtn_0d_usa
SELECT cities.id, cities.name, states.name AS name 
FROM states INNER JOIN cities
ON cities.state_id = states.id
ORDER BY cities.id ASC;
