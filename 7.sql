SELECT title, rating
FROM movies
JOIN ratings
on movies.id= ratings.movie_id
Where year =2010
ORDER BY rating DESC, title;