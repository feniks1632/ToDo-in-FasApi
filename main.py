from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4


app = FastAPI(
    title='To-Do List ib FastApi',
    description='Простая апишка для управления задачами',
    version=1.0
)