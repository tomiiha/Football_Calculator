# Code to import fbref files for SQL db creation.
# Right now running on a local instance only, will check cloud comp later.

# Packages
import sqlite3 as sq

# set SQL - 'football.db' as a repository.
connection = sq.connect("football.db")
