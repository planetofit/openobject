#sql
#https://towardsdatascience.com/yes-python-has-a-built-in-database-heres-how-to-use-it-b3c033f172d3
#import os
import sqlite3

# create a connection
conn = sqlite3.connect('zelda.db')

# create a table
c = conn.cursor()  # cursor

c.execute("""CREATE TABLE ZeldaId (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time TIMESTAMP,
            x REAL,
            y REAL,
            z REAL
    )""")
    
# commit
conn.commit()

# close the connection
conn.close()