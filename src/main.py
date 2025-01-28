from fastapi import FastAPI
from typing import Optional 
from modules.tasks_operations import create_task, get_tasks, get_task_by_id, update_task, delete_task
from common.models import Task, Status

app = FastAPI()

@app.post("/tasks")
def create_new_task(task: Task):
    return create_task(task)

@app.get("/tasks")
def get_all_tasks(status: Optional[Status] = None):
    return get_tasks(status=status)

@app.get("/tasks/{task_id}")
def get_task_details(task_id: int):
    return get_task_by_id(task_id)

@app.put("/tasks/{task_id}")
def update_existing_task(task_id: int, updated_task: Task):
    return update_task(task_id, updated_task)

@app.delete("/tasks/{task_id}")
def delete_task_by_id(task_id: int):
    delete_task(task_id)
    return {"message": "Task deleted successfully"}