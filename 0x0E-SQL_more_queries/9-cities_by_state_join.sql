-- Displaying all the cities and their various states

SELECT c.id, c.name AS name, s.name AS name
FROM cities c INNER JOIN states s
    ON c.state_id = s.id
ORDER BY c.id ASC;