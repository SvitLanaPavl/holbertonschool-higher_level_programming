-- Lists all the cities of California that can be found on the database
SELECT hbtn_0d_usa.cities.id, hbtn_0d_usa.cities.name
WHERE state_id IN (SELECT states.id WHERE name = California) ORDER BY id ASC;
