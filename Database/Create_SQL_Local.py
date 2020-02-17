# Code to import fbref files for SQL db creation.
# Right now running on a local instance only, will check cloud comp later.
# Look into eventually PW protecting the DB, although might not be necessary.

# Packages
import sqlite3 as sq

# set SQL - 'football.db' as a repository.
connection = sq.connect("football.db")
