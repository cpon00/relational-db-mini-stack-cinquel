# Movie Dataset

<a href = "https://www.kaggle.com/tmdb/tmdb-movie-metadata">TMDB 5000 Movie Dataset Link </a>

## What the dataset contains:

This dataset contains data from about 5000 well known American movies, with unique json values for each specific movie.

## What applications would find the dataset useful?

Applications that might find this dataset useful could be film review sites that need to list movies organized by a particular genre, cast member, producer, director, year, etc. We may even be able to predict which films may be highly rated in the future, given the popularity score, and revenue.

## What kinds of questions might such applications ask of this dataset?

Our datasets could answer questions such as, "How many movies are about pirates?" or "How many movie titles contain the word 'dog' that are in the action genre? Given a wide variety of questions, our application will return accurate results to the user.

# Tables

- movie

  - id
  - original language
  - title
  - popularity
  - release_date
  - vote_average
  - vote_count

- moviegenre

  - movie_id
  - genre_id

- genre

  - genre_id
  - genre_name

- character

  - movie_id
  - actor_id
  - character_name
  - gender
  - char_order

- actor

  - actor_id
  - name

- moviekeyword

  - movie_id
  - keyword_id

- keyword

  - keyword_id
  - keyword_name

Our datasets could answer questions such as, "How many movies are about pirates?" or "How many movie titles contain the word 'dog'? Given a wide variety of questions, our application will return accurate results to the user.

## Instructions

1.  Ensure you have proper modules installed.
2.  Initialize database, then load schema.
3.  Run main_loader.py. This will populate tables `movie`, `genre`, `moviegenre`, `keyword`, and `moviekeyword`.
4.  Run credit_loader.py. This will populate tables `actor` and `character`.
5.  Run queries!
