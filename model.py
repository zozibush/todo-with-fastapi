from pydantic import BaseModel, Optional
from typing import List
from fastapi import Form

class Todo(BaseModel):
    id: int
    item: str

class TodoItem(BaseModel):
    id: Optional[int]
    item: str

    @classmethod
    def as_form(cls, item: str = Form(...)):
        return cls(item=item)
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