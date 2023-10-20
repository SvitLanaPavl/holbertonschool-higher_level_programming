-- Lists all genres from hbtn_0d_tvshows and displays shows linked to each other
SELECT tv_show_genres.name AS genre,
COUNT(show_id) AS number_of_shows
FROM tv_genres
JOIN tv_shows_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre
ORDER BY number_of_shows DESC;
