from pydantic import BaseModel
from typing import List

class Todo(BaseModel):
    id: int
    item: str

class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {"item": "Read the next chapter of the book."}
        }

class TodoItems(BaseModel):
    todos: List[Todo]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {"id": 1, "item": "Example schema 1!"},
                    {"id": 2, "item": "Example schema 2!"},
                ]
            }
        }