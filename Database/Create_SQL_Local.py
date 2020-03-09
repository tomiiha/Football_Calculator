# Code to import fbref files for SQL db creation.
# Right now running on a local instance only, will check cloud comp later.
# Look into eventually PW protecting the DB, although might not be necessary.

# Packages
import sqlite3 as sq
import csv
import os


# Get files first for batch processing
data_files = []
file_list = os.listdir()
for x in file_list:
    if x[-4:] == '.csv':
        data_files.append(x)

print(data_files)

# set SQL - 'football.db' as a repository.
conn = sq.connect("football.db")
cur = conn.cursor()
cur.execute("CREATE TABLE")
