-- Lists all the cities of California that can be found on the database
SELECT cities.id, cities.name
WHERE state_id = (SELECT states.id WHERE name = 'California');
