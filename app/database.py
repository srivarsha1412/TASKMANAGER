
from motor.motor_asyncio import AsyncIOMotorClient
MONGO_URI = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URI)
db = client["taskmanager"]  # Database name: 'taskmanager'
task_collection = db["tasks"]  # Collection name: 'tasks' 
