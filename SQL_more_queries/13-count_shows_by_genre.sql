-- Lists all genres from hbtn_0d_tvshows and displays shows linked to each other
SELECT tv_show_genres.name AS genre,
COUNT(*) AS number_of_shows
FROM tv_genres AS tv_show_genres
LEFT JOIN tv_shows_genres ON tv_show_genres.show_id = tv_shows.id
GROUP BY tv_show_genres.name
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;
