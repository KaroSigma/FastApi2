from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional

class Status(Enum):
    TODO = "to do"
    INPROGRESS = "in progress"
    FINISHED = "finished"

class Task(BaseModel):
    id: int
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=300)
    status: Status = Status.TODO