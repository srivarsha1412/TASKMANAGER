from datetime import datetime
from bson import ObjectId
from .database import task_collection  
import random


# Function to generate a unique task ID (we use a random number here for simplicity)
async def generate_task_id(): 
    while True:
        task_id = random.randint(1000, 9999)
        if not await task_collection.find_one({"_id": task_id}):
            return task_id


# Serialize task data to ensure proper format
def serialize_task(task):
    return {
        "_id": str(task["_id"]),
        "task_name": task["task_name"],
        "status": task["status"],
        "created_at": task["created_at"],
    }


# Function to create a new task
async def create_task(task_name: str):
    if not task_name.strip():
        raise ValueError("Task name cannot be empty.")
    
    task = {
        "_id": await generate_task_id(),  # Ensure the task ID is unique
        "task_name": task_name,
        "status": "Running",  # Simulate forking by setting status to 'Running'
        "created_at": datetime.utcnow()  # Current timestamp
    }
    
    try:
        result = await task_collection.insert_one(task)
        return serialize_task(task)
    except Exception as e:
        raise Exception(f"Failed to create task: {str(e)}")


# Function to fetch all tasks
async def get_tasks():
    tasks = []
    try:
        cursor = task_collection.find({})
        async for task in cursor:
            tasks.append(serialize_task(task))
        return tasks
    except Exception as e:
        raise Exception(f"Error fetching tasks: {str(e)}")    
    
    
