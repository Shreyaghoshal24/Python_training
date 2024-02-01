from fastapi import FastAPI
import uvicorn

app = FastAPI()

users = {1: "Shreya"}
user_id_counter = 2


@app.get("/get_users")
def get_users():
    return users


@app.post("/add_user/{user_name}")
def add_user(user_name: str):
    global user_id_counter
    user_id = user_id_counter
    users[user_id] = user_name
    user_id_counter += 1
    return {"message": "User added successfully", "user_id": user_id, "user_name": user_name}


@app.put("/update_user/{user_id}/{user_name}")
def update_user(user_id: int, user_name: str):
    if user_id in users:
        users[user_id] = user_name
        return {"message": "User updated successfully", "user_id": user_id, "user_name": user_name}
    else:
        return {"error": "User not found"}


@app.delete("/delete_user/{user_id}")
def delete_user(user_id: int):
    if user_id in users:
        deleted_user = users.pop(user_id)
        return {"message": "User deleted successfully", "deleted_user": deleted_user}
    else:
        return {"error": "User not found"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

