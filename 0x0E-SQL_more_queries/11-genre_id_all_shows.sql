-- Retrieving all shows including those without a genre and set them to NULL

SELECT title, genre_id
FROM tv_shows s LEFT JOIN tv_show_genres g
ON s.id = g.show_id
ORDER BY title ASC, genre_id ASC;