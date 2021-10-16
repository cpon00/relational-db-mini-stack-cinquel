import json
import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy
import psycopg2
import io
import time


def movie_loader(path):
    df = pd.read_csv(path)
    df["release_date"] = pd.to_datetime(
        df["release_date"]).apply(lambda x: x.date())
    json.columns = [
        "genres",
        "keywords",
        "production_countries",
        "production_companies",
    ]
    for column in json.columns:
        df[column] = df[column].apply(json.loads)
    return df


# def credits_loader(path):
#     df = pd.read_csv(path)
#     json_columns = ["cast", "crew"]
#     for column in json_columns:
#         df[column] = df[column].apply(json.loads)
#     return df


movies = pd.read_csv(
    "C:\\Users\\cpon7\\Desktop\\relational-db-mini-stack-cinquel\\tmdb_5000_movies.csv")
# credits = credits_loader("./tmdb_5000_credits.csv")

print(movies.head(10).genres)
# print(credits.head(10))

# Cast Keys
# print(sorted(credits.cast.iloc[0][0].keys()))

# Crew Keys
# print(sorted(credits.crew.iloc[0][0].keys()))

# credits.apply(
#     lambda row: [x.update({"movie_id": row["movie_id"]}) for x in row["cast"]], axis=1
# )
# credits.apply(
#     lambda row: [x.update({"movie_id": row["movie_id"]}) for x in row["crew"]], axis=1
# )
# credits.apply(
#     lambda row: [
#         person.update({"order": order}) for order, person in enumerate(row["crew"])
#     ],
#     axis=1,
# )

# cast = []
# credits.cast.apply(lambda x: cast.extend(x))
# cast = pd.DataFrame(cast)
# cast["type"] = "cast"

# crew = []
# credits.crew.apply(lambda x: crew.extend(x))
# crew = pd.DataFrame(crew)
# crew["type"] = "crew"

# people = pd.concat([cast, crew], ignore_index=True)

# conn_string = "postgresql://localhost/postgres"
# db = create_engine(conn_string)
# conn = db.connect()

# sql = '''
# COPY copy_test
# FROM 'C:\\Users\\cpon7\\Desktop\\relational-db-mini-stack-cinquel\\tmdb_5000_movies.csv'
# DELIMITER ',' CSV;
# '''

# table_create_sql = '''
# CREATE TABLE IF NOT EXISTS copy_test (
#     id                int,
#     budget            int,
#     original_language VARCHAR,
#     title             VARCHAR,
#     popularity        double precision,
#     release_date      DATE,
#     revenue           int,
#     runtime           int,
#     tagline           VARCHAR,
#     vote_average      double precision,
#     vote_count        int
# )
# '''

# pg_conn = psycopg2.connect(conn_string)
# cur = pg_conn.cursor()
# cur.execute(table_create_sql)
# cur.execute('TRUNCATE TABLE copy_test')
# start_time = time.time()
# movies.to_csv('tmdb_5000_movies.csv', index=False, header=False)
# cur.execute(sql)
# pg_conn.commit()
# cur.close()
# print("COPY duration: {} seconds".format(time.time() - start_time))
# conn.close()
