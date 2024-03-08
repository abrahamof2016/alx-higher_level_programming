-- A Script that lists all shows contained in hbtn_0d_tvshows
-- that have at least on genre linked.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
NATURAL JOIN tv_show_genres
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
