import json
import pandas as pd
import csv
import sys


def formatter(path):
    df = pd.read_csv(path)
    json_columns = ['cast', 'crew']
    for column in json_columns:
        df[column] = df[column].apply(json.loads)
    return df


credits = formatter("./tmdb_5000_credits.csv")

actors = {}
for cast in credits.cast:
    end = 2 if len(cast) > 3 else len(cast)
    for character in cast:
        actor_id = character['id']
        name = character['name'].replace("'", "''")
        actors[actor_id] = name

for (key, value) in actors.items():
    print(
        f'INSERT INTO actor VALUES({key},\'{value}\');')

    # actor_id = cast[i]['id']
    # cast_id = cast[i]['cast_id']
    # character_name = cast[i]['character']
    # order = cast[i]['order']


for (movie_id, cast) in zip(credits.movie_id, credits.cast):
    end = 2 if len(cast) > 3 else len(cast)
    for character in cast:
        actor_id = character['id']
        character_name = character['character'].replace("'", "''")
        gender = character['gender']
        order = character['order']
        if order > end:
            break
        else:
            print(
                f'INSERT INTO character VALUES({movie_id},{actor_id},\'{character_name}\', {gender}, {order});')
