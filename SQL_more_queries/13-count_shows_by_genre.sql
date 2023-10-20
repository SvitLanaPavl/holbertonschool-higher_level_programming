-- Lists all genres from hbtn_0d_tvshows and displays shows linked to each other
SELECT genres.genre AS genre,
COUNT(tv_shows.show_id) AS number_of_shows
FROM genres
LEFT JOIN tv_shows_genres ON tv_show_genres.show_id = tv_shows.id
GROUP BY genres.genre
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;
