from pydantic import BaseModel, Field   
from datetime import datetime
from typing import Optional

#Task input model for creating new tasks
class TaskCreate(BaseModel): 
    task_name: str   


# Task output model returned to the user
class TaskResponse(BaseModel):
    id: str = Field(alias="_id")
    task_name: str
    status: str
    created_at: datetime

    class Config:
        json_encoders = {
            datetime: lambda dt: dt.isoformat(),
        }
        allow_population_by_field_name = True 
