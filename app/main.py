from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from app.models import TaskCreate, TaskResponse
from app.crud  import get_tasks, create_task 


#Initialize the FastAPI app
app = FastAPI(title="Task Manager")


# Endpoint to get a list of all tasks
@app.get("/tasks", response_model=list[TaskResponse])
async def read_tasks():
    try:
        tasks = await get_tasks()
        return tasks  # Returning empty list is fine!
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Something went wrong while fetching tasks: {str(e)}"}
        )

# Endpoint to create a new task
@app.post("/tasks", response_model=TaskResponse)
async def create_task(task: TaskCreate):
    try:
        if not task.task_name.strip():
            raise HTTPException(status_code=400, detail="Task name cannot be empty.")
        
        # Create the task and return it as a JSON response
        new_task = await create_task(task.task_name)
        return new_task  # Returning the created task as JSON

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Something went wrong while creating the task: {str(e)}"}
        )


