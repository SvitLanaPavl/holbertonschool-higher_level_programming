-- Lists all genres from hbtn_0d_tvshows and displays shows linked to each other
SELECT genre AS 'TV Show genre',
COUNT(tv_shows.title) AS 'Number of shows linked to this genre'
FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
GROUP BY genre
ORDER BY COUNT(tv_shows.title) DESC;
