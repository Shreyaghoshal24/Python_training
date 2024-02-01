# from typing import Union

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

# //simple get method
# from fastapi import FastAPI

# app = FastAPI()

# //to create new items & print the complete data
# @app.get("/Hello")
# async def root():
#     return {"message": "World"}

# //path parameters
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_item(item_id):               
#     return {"item_id": item_id}

# //Path parameters with types
# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

# //Using pydantic to Declare JSON Data Models (Data Shapes)

# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None

# app = FastAPI()

# @app.post("/items/")
# async def create_item(item: Item):
#     return item
