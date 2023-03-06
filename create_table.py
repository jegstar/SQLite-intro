# Import the SQLite functions
import sqlite3

# Connects to a database. If it doesn't exist, we can write SQL to create it
conn = sqlite3.connect('my_database.db')

# We will want to perform many commands, so we use a cursor to do that.
cur = conn.cursor()




# We should close the connection that we had at the beginning to ensure data integrity.
conn.close()