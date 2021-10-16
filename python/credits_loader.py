import csv
import sys

"""
This program generates direct SQL statements from the source Netflix Prize files in order
to populate a relational database with those files’ data.

By taking the approach of emitting SQL statements directly, we bypass the need to import
some kind of database library for the loading process, instead passing the statements
directly into a database command line utility such as `psql`.
"""

# The INSERT approach is best used with a transaction. An introductory definition:
# instead of “saving” (committing) after every statement, a transaction waits on a
# commit until we issue the `COMMIT` command.
# print('BEGIN;')

sys.stdout.reconfigure(encoding='utf-8')
# For simplicity, we assume that the program runs where the files are located.
MOVIE_SOURCE = 'tmdb_5000_credits.csv'
with open(MOVIE_SOURCE, 'r+', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        id = int(float(row[3])) if row[3] != '' else None
        if not id:
            continue
        original_language = row[5]
        title = row[17]
        popularity = row[8]
        release_date = row[11]
        runtime = int(float(row[13])) if row[13] != '' else 0
        vote_average = row[18]
        vote_count = int(float(row[19]))

        # Watch out---titles might have apostrophes!
        title = title.replace("'", "''")
        print(
            f'INSERT INTO movie VALUES({id}, \'{original_language}\', \'{title}\', {popularity}, \'{release_date}\', {runtime}, {vote_average}, {vote_count});')


# We wrap up by emitting an SQL statement that will update the database’s movie ID
# counter based on the largest one that has been loaded so far.
print('SELECT setval(\'movie_id_seq\', (SELECT MAX(id) from movie));')

# _Now_ we can commit our transation.
print('COMMIT;')
