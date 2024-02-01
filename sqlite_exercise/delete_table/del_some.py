import sqlite3

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('geek.db')

# cursor object
cursor_obj = connection_obj.cursor()


#delete data
cursor_obj.execute("DELETE FROM GEEK WHERE Score < 15")

connection_obj.commit()
# Close the connection
connection_obj.close()
