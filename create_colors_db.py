import sqlite3
conn = sqlite3.connect('colors.db') # Warning: This file is created in the current directory
conn.execute("CREATE TABLE colors (id INTEGER PRIMARY KEY, color char(100) NOT NULL, flower char(100) NOT NULL)")
conn.execute("INSERT INTO colors (color,flower) VALUES ('Pink','Rose')")
conn.execute("INSERT INTO colors (color,flower) VALUES ('Yellow','Sunflower')")
conn.execute("INSERT INTO colors (color,flower) VALUES ('White','Lily')")
conn.execute("INSERT INTO colors (color,flower) VALUES ('Red','Hibiscus')")
conn.commit()