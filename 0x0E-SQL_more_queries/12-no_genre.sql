-- Retrives all shows without genre

SELECT title, genre_id
FROM tv_shows s LEFT JOIN tv_show_genres g
ON id = show_id
WHERE genre_id IS NULL
ORDER BY title ASC, genre_id ASC;