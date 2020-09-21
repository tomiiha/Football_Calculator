# Import https://www.github.com/jalapic/engsoccerdata csv file.

import sqlite3 as sq
import pandas as pd

conn = sq.connect("eng_full_hist.db")
csv_file = 'england.csv'
table_name = 'eng_full_hist'
df = pd.read_csv(csv_file)
df.to_sql(table_name, conn, if_exists='append', index=False)
