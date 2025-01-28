from enum import Enum
from typing import Optional
from sqlmodel import SQLModel, Field

class Status(Enum):
    TODO = "to do"
    INPROGRESS = "in progress"
    FINISHED = "finished"

class Task(SQLModel, table=True):
    id: int
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=300)
    status: Status = Status.TODO