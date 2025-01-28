from common.models import Task, Status
from typing import List, Optional
from fastapi import HTTPException

tasks: List[Task] = []

def create_task(task: Task) -> Task:
    for existing_task in tasks:
        if existing_task.title == task.title:
            raise HTTPException(status_code=400, detail="Task title must be unique")
    
    task.id = len(tasks) + 1
    tasks.append(task)
    return task

def get_tasks(status: Optional[Status] = None) -> List[Task]:
    if status:
        return [task for task in tasks if task.status == status]
    return tasks 

def get_task_by_id(task_id: int) -> Task:
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

def update_task(task_id: int, updated_task: Task) -> Task:
    task = next((task for task in tasks if task.id == task_id), None)
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    for existing_task in tasks:
        if existing_task.title == updated_task.title and existing_task.id != task_id:
            raise HTTPException(status_code=400, detail="Task title must be unique")
    
    task.title = updated_task.title
    task.description = updated_task.description
    task.status = updated_task.status
    
    return task

def delete_task(task_id: int) -> None:
    task = next((task for task in tasks if task.id == task_id), None)
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    tasks.remove(task)