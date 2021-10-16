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

for (item) in credits.cast:
    end = 1 if len(item) >= 3 else len(item)
    for i in range(0, end):
        print(item[i]['name'], item[i]['character'])
