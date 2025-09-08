from fastapi import APIRouter, HTTPException
from typing import List, Optional
from uuid import uuid4
from models import TodoItem


router = APIRouter(
    prefix="/todos", # Общий префикс для всех путей 
    tags=["Задачи"], # для группировки в документации
)

# Хранилище (временно в памяти)
todos_db: List[TodoItem] = []

# Create

@router.post("/", response_model=TodoItem, summary='Создать новую задачу')
async def create_todo(todo: TodoItem):
    if not todo.id:
        todo.id = str(uuid4())
    todos_db.append(todo)
    return todo

# Get all    
@router.get("/", response_model=List[TodoItem], summary='Получить список всех задач')
async def get_todos(completed: Optional[bool] = None):
    if completed is not None:
        return [todo for todo in todos_db if todo.completed == completed]
    return todos_db

# Get one

@router.get("/{todo_id}", response_model=TodoItem, summary='Получить задачу по ID')
async def get_todo(todo_id: str):
    for todo in todos_db:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail='Задача не найдена')

# Update todo
@router.put("/{todo_id}", response_model=TodoItem, summary='Обновить задачу по ID')
async def update_todo(todo_id: str, updated_todo: TodoItem):
    for index, todo in enumerate(todos_db):
        if todo.id == todo_id:
            updated_todo.id = todo_id
            todos_db[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail='Задача не найдена')
    
# Delete todo
@router.delete("/{todo_id}", summary='Удалить задачу по ID')
async def delete_todo(todo_id: str):
    for index, todo in enumerate(todos_db):
        if todo.id == todo_id:
            todos_db.pop(index)
            return {"message": "Задача удалена"}
    raise HTTPException(status_code=404, detail='Задача не найдена')
    
     
    