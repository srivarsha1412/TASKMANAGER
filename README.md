This is a simple FastAPI-based Task Manager inspired by Unix-like system commands. It allows you to create and list tasks similar to how you  use `fork` and `ls` in a Unix environment. 

List all tasks (`GET /tasks`) — like `ls`
Create a new task (`POST /tasks`) — like `fork` 

MongoDB is used as the backend to persist task data. 

UNIX_TASK_MANAGER
├── app
│   ├── main.py
│   ├── models.py
│   ├── crud.py
│   └── database.py
├── requirements.txt
└── README.md   

### setup instruction 

step1 : Create a Virtual Environment  
            python -m venv venv
            source venv/bin/activate  # Windows  

step2 : Install dependencies 
            pip install -r requirements.txt
 
step3 : Setup MongoDB  # Make sure Mongodb is running locally 

### Running the app
uvicorn app.main:app --reload    ## tells uvicorn where to searn FastAPI  

uvicorn - server that runs FastAPI 
app     - folder containing your main.py
main    - FastAPI instance in main.py file
app     - FastAPI app instance created in main.py
           
           


