import sqlite3

# Connect to SQLite database (or create a new one if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table (if it doesn't exist)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
''')

# Commit the changes and close the connection
conn.commit()

# Create
def create_user(name, age):
    cursor.execute('''
        INSERT INTO users (name, age)
        VALUES (?, ?)
    ''', (name, age))
    conn.commit()

# Read
def read_users():
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Update
def update_user(user_id, new_age):
    cursor.execute('''
        UPDATE users
        SET age = ?
        WHERE id = ?
    ''', (new_age, user_id))
    conn.commit()

# Delete
def delete_user(user_id):
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()

# Example usage
create_user('Shreya Ghoshal', 24)
create_user('Shreyansh Ghoshal', 18)
read_users()

update_user(1, 26)
read_users()

delete_user(2)
read_users()

# Close the connection when done
conn.close()
