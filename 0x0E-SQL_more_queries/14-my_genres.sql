-- retrieves all Dexter shows
SELECT name
FROM tv_genres g INNER JOIN tv_show_genres sg 
ON g.id = genre_id
INNER JOIN tv_shows s
ON s.id = show_id
WHERE title = "Dexter"
ORDER BY name ASC;