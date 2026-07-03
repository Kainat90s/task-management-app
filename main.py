from fastapi import FastAPI
from src.utils.db import Base, engine
from src.tasks.model import Task
from src.users.model import User
from src.tasks.router import task_routes
from src.users.router import user_routes
from src.admin.router import admin_routes
Base.metadata.create_all(engine)

app=FastAPI(title="Task Management System")
app.include_router(task_routes)
app.include_router(user_routes)
app.include_router(admin_routes)