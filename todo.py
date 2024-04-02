from fastapi import APIRouter

todo_router = APIRouter()

todo_list = []

@todo_router.post("/todo")
async def add_todo(todo: str) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}

@todo_router.get("/todo")
async def get_todo() -> dict:
    return {"todo_list": todo_list}
