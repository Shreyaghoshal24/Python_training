from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import uvicorn

def create_connection():
    connection = sqlite3.connect("movies.db")
    return connection

def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    director TEXT NOT NULL
    )
    """)
    connection.commit()
    connection.close()

create_table()  

class MovieCreate(BaseModel):
    title: str
    director: str

class Movie(MovieCreate):
    id: int

app = FastAPI()

@app.get("/")
def read_root():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()
    connection.close()
    return {"movies": movies}

def create_movie(movie: MovieCreate):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO movies (title, director) VALUES (?, ?)", (movie.title, movie.director))
    connection.commit()
    movie_id = cursor.lastrowid
    connection.close()
    return movie_id

@app.post("/movies/")
def create_movie_endpoint(movie: MovieCreate):
    movie_id = create_movie(movie)
    return {"id": movie_id, **movie.dict()}

@app.get("/movies/{movie_id}")
def read_movie(movie_id: int):
    movie = get_movie(movie_id)
    if movie:
        return {"id": movie[0], "title": movie[1], "director": movie[2]}
    else:
        raise HTTPException(status_code=404, detail="Movie not found")

def get_movie(movie_id: int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM movies WHERE id = ?", (movie_id,))
    movie = cursor.fetchone()
    connection.close()
    return movie

def update_movie(movie_id: int, updated_movie: MovieCreate):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE movies SET title = ?, director = ? WHERE id = ?", (updated_movie.title, updated_movie.director, movie_id))
    connection.commit()
    connection.close()

def delete_movie(movie_id: int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
    connection.commit()
    cursor.execute("VACUUM")  # to overcome this id issue used vacuum, it will compact the database to reorganize the IDs
    connection.close()

@app.put("/movies/{movie_id}")
def update_movie_endpoint(movie_id: int, updated_movie: MovieCreate):
    existing_movie = get_movie(movie_id)
    if existing_movie:
        update_movie(movie_id, updated_movie)
        return {"id": movie_id, **updated_movie.dict()}
    else:
        raise HTTPException(status_code=404, detail="Movie not found")

@app.delete("/movies/{movie_id}")
def delete_movie_endpoint(movie_id: int):
    existing_movie = get_movie(movie_id)
    if existing_movie:
        delete_movie(movie_id)
        return {"message": "Movie deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Movie not found")

if __name__ == "__main__":
    uvicorn.run("test:app", host="127.0.0.1", port=8000, reload=True)
