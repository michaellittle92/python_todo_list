from fastapi import FastAPI, HTTPException
from taskmanger import *
from task import Task

InitializeDatabase()

app = FastAPI()

@app.get("/")
async def root():
    return{"message": "Root api location"}

@app.get("/get-all-tasks")
async def Get_All_Tasks():
    all_tasks = TaskManager.get_all_tasks()
    return all_tasks

@app.get("/get-all-incomplete-tasks")
async def Get_All_Incomplete_Tasks():
    all_tasks = TaskManager.get_all_incomplete_tasks()
    return all_tasks

@app.post("/add_task")
async def add_task(task_name:str):
    Task(0, task_name, False).create_new_task()


@app.patch("/complete_task")
async def mark_complete(task_id:int):
   task = Task.get_task_by_id(task_id)
   if task is None:
       raise HTTPException(status_code=404, detail="Task not found")
   task.mark_complete()
   return{"message": f"Task {task_id} marked as complete"}