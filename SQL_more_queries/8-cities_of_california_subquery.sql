-- Lists all the cities of California that can be found on the database
SELECT cities.id, cities.name
WHERE state_id IN (SELECT states.id WHERE name = 'California') ORDER BY id ASC;
