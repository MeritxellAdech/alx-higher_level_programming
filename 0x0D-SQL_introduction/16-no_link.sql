-- Displaying the data in the second_table in ascending order
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
