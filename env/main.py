from enum import Enum
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

class Category (Enum):
    PERSONAL = 'personal'
    WORK = 'work'

class Todo(BaseModel):
    title: str
    complete: bool
    id: int
    category: Category

todos = {
    1: Todo(title="Buy milk", complete=False, id=1, category=Category.PERSONAL),
    2: Todo(title="Buy bread", complete=False, id=2, category=Category.WORK),
    3: Todo(title="Buy cheese", complete=False, id=3, category=Category.PERSONAL),
    4: Todo(title="Buy pasta", complete=False, id=4, category=Category.WORK),
    5: Todo(title="Buy eggs", complete=False, id=5, category=Category.PERSONAL),
    6: Todo(title="Buy cheese", complete=False, id=6, category=Category.WORK),
    }

@app.get("/")
def index() -> dict[str, dict[int, Todo]]:
    return {"todos": todos}

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int) -> Todo:
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos[todo_id]

@app.post("/todos")
def query_todo_by_completed(completed: bool | None ) -> dict[str,list[Todo]]:
    filtered_todos = [todo for todo in todos.values() if todo.complete == completed]
    return {"todos": filtered_todos}


