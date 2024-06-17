-- Retrieving all comedy shows
SELECT title
FROM tv_genres g INNER JOIN tv_show_genres sg
ON g.id = genre_id
INNER JOIN tv_shows s
ON show_id = s.id
WHERE name = "Comedy"
ORDER BY title ASC;