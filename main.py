from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

from routers.todos import router as todos_router

app = FastAPI(
    title='To-Do List ib FastApi',
    description='Простая апишка для управления задачами',
)

app.include_router(todos_router)