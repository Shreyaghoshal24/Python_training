from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import uvicorn

app = FastAPI()

DATABASE_FILE = "test.db"

def create_users_table():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

create_users_table()

class UserAuth(BaseModel):
    id: int
    password: str

@app.post("/register-user", tags=["User Registration"])
async def register_user(user: UserAuth):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO users (id, password) VALUES (?, ?)''',
                   (user.id, user.password))
    conn.commit()
    conn.close()

    return {"message": "User registered successfully"}

@app.post("/login-user", tags=["User Login"])
async def login_user(user: UserAuth):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute('''SELECT id, password FROM users WHERE id=?''',
                   (user.id,))
    result = cursor.fetchone()

    conn.close()

    if result:
        stored_password = result[1]
        if user.password == stored_password:
            return {"message": "Login successful"}
        else:
            raise HTTPException(
                status_code=401, detail="Either ID or password is wrong")
    else:
        raise HTTPException(status_code=401, detail="Login failed")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
