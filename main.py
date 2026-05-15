from fastapi import FastAPI
from src.utils.db import Base, engine
from src.tasks.model import Task
from src.users.model import User
from src.tasks.router import task_routes
Base.metadata.create_all(engine)
app=FastAPI(title="Task Management System")
app.include_router(task_routes)