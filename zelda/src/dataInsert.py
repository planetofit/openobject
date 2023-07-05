#import os
import sqlite3
from datetime import datetime

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# create a connection
conn = sqlite3.connect('zelda.db')

# start a cursor
c = conn.cursor()

# insert data into a table
#c.execute("INSERT INTO ZeldaId VALUES (datetime.now(), 1,1,1)")

#Run a loop to build a dataset and insert in the table
i = 10
all_zeldas = []
while i < 20:
    all_zeldas += [
    (datetime.now(), i, i, i)
    ]
    i += 1

c.executemany("INSERT INTO ZeldaId (time, x, y, z) VALUES (?, ?, ?, ?)", all_zeldas)

# insert data into a table
#c.execute("INSERT INTO ZeldaId VALUES (datetime.now(), 1,1,1)")
#c.executemany("INSERT INTO ZeldaId VALUES (?, ?, )", all_zeldaIds)

# commit
conn.commit()

# close the connection
conn.close()
