from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4


class TodoItem(BaseModel):
    id: str 
    title: str
    description: Optional[str] = None
    completed: bool = False


# Временное хранилище — список задач
todos_db: List[TodoItem] = []