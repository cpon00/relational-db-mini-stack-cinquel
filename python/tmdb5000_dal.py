import os

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, Double, ForeignKey, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import select, func
from sqlalchemy.orm import sessionmaker, relationship

db = create_engine(os.environ['DB_URL'])
metadata = MetaData(db)
movie_table = Table('movie', metadata, autoload=True)
credit_table = Table('credit', metadata, autoload=True)
#rating_table = Table('rating', metadata, autoload=True)


# Raw SQL-style implementation of a movie query.
def search_movies_by_title(query, limit=100):
    with db.connect() as connection:
        # We want actual %'s so need to escape them in the string.
        result_set = connection.execute(f"""
            SELECT * FROM movie WHERE title ILIKE '%%{query}%%' ORDER BY title LIMIT {limit}
        """)
        result = result_set.fetchall()
        return list(result)


# SQL builder-style implementation of an aggregate query.
# def get_average_rating_of_movie(movie_id):
#     with db.connect() as connection:
#         statement = select([func.avg(rating_table.c.rating)]).where(rating_table.c.movie_id == movie_id)
#         result_set = connection.execute(statement)

#         # We know in advance that this will be a single row with a single column so we feel safe about hardcoding this.
#         # A non-existent movie will yield `None` for this expression.
#         return result_set.fetchone()[0]


# For ORM-style implementations, we need to define a few things first.
ORM_Base = declarative_base()

# 3original_language, title, popularity, release_date, runtime, vote_average, vote_count
class Movie(ORM_Base):
    __tablename__ = 'movie'
    id = Column(Integer, Sequence('movie_id_seq'), primary_key=True)
    original_language = Column(String)
    title = Column(String)
    popularity = Column(Double)
    release_date = Column(Date) #how to format date?
    runtime = Column(Integer)
    vote_average = Column(Double)
    vote_count = Column(Integer)

class Genre(ORM_Base):
    __tablename__ = 'genre'
    genre_id = Column(Integer, Sequence('genre_id_seq'), primary_key=True) #idk
    genre_name = Column(Integer)

class MovieGenre(ORM_Base):
    __tablename__ = 'moviegenre'
    movie_id = Column(Integer, ForeignKey('movie.id'), primary_key=True)
    genre_id = Column(Integer)

class Character(ORM_Base):
    __tablename__ = 'character'
    movie_id = Column(Integer, ForeignKey('movie.id'), primary_key=True)
    actor_id = Column(Integer),
    cast_id = Column(Integer)
    character_name = Column(String)
    gender = Column(Integer)
    
class Actor(ORM_Base):
    __tablename__ = 'actor'
    id = Column(Integer, Sequence('movie_id_seq'), primary_key=True)
    name = Column(String)

class Keyword(ORM_Base):
    __tablename__ = 'keyword'
    id = Column(Integer, , primary_key=True)
    keyword_name = Column(String)

class MovieKeyword(ORM_Base):
    __tablename__ = 'moviekeyword'
    movie_id = Column(Integer, , primary_key=True)
    keyword_id = Column(Integer, ForeignKey('keyword.id'))
    

# class Rating(ORM_Base):
#     __tablename__ = 'rating'

#     # ORM requires some way to guarantee the uniqueness of a row, even if the table itself doesn’t have an official
#     # primary key. By marking multiple columns as a “primary_key,” we’re telling ORM that the _combination_ of these
#     # values can uniquely identify a row.
#     #
#     # In our case, we are making the explicit choice that no viewer can rate the same movie more than once.
#     # Fortunately, this appears to be true for the given dataset.
#     movie_id = Column(Integer, ForeignKey('movie.id'), primary_key=True) # ForeignKey takes table properties…
#     viewer_id = Column(Integer, primary_key=True)
#     rating = Column(Integer)
#     date_rated = Column(Date)
#     movie = relationship('Movie') # …but relationship takes the mapped class


# The notion of a Session is a multifaceted one whose usage and implementation may change depending on the type
# of application that is using this DAL (particularly, a standalone application vs. a web service). It is implemented
# here in the simplest possible way. Note that if this DAL is to be used in other contexts, code surrounding sessions
# may have to change.
#
# At a minimum, we follow the basic SQLAlchemy rule that sessions should be external to the functions that use them.
# Thus, we define current_session at this upper level, and not within each function.
Session = sessionmaker(bind=db)
current_session = Session()


# ORM-style implementation of a rating query.
# def get_ratings_by_viewer(viewer_id, limit=100):
#     query = current_session.query(Rating).\
#         join(Movie).\
#         filter(Rating.viewer_id == viewer_id).\
#         order_by(Rating.date_rated, Movie.title).\
#         limit(limit)

#     return query.all()


# ORM-style implementation of a movie inserter.
# i think this should work?? idk i just changed the args -josh
def insert_movie(original_language, title, popularity, release_date, runtime, vote_average, vote_count):
    movie = Movie(original_language=original_language, title=title, popularity=popularity, release_date=release_date, runtime=runtime, vote_average=vote_average, vote_count=vote_count)
    current_session.add(movie)
    current_session.commit() # Make the change permanent.
    return movie