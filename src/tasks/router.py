# from fastapi import APIRouter,Depends
# from src.tasks import controller
# from src.tasks.dtos import TaskSchema
# from src.utils.db import get_db

# task_routes = APIRouter(prefix="/tasks")

# @task_routes.post("/create")
# def create_task(body:TaskSchema, db=Depends(get_db)):
#     return controller.create_task(body,db)

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.tasks import controller
from src.tasks.dtos import TaskSchema
from src.utils.db import get_db
from src.utils.hepers import is_authenticated  # 👈 protected route ke liye

task_routes = APIRouter(prefix="/tasks")


@task_routes.post("/create", status_code=status.HTTP_201_CREATED)
def create_task(body: TaskSchema, db: Session = Depends(get_db), user=Depends(is_authenticated)):
    print(user)
    return controller.create_task(body, db, user.id)


@task_routes.get("/my_tasks", status_code=status.HTTP_200_OK)
def get_my_tasks(db: Session = Depends(get_db), user=Depends(is_authenticated)):
    return controller.get_user_tasks(db, user.id)

@task_routes.get("/all_tasks", status_code=status.HTTP_200_OK)
def get_all_tasks(db: Session = Depends(get_db), user=Depends(is_authenticated)):
    return controller.get_all_tasks(db)

@task_routes.get("/{task_id}", status_code=status.HTTP_200_OK)
def get_task(task_id: int, db: Session = Depends(get_db), user=Depends(is_authenticated)):
    return controller.get_specific_task(task_id, db, user.id)


@task_routes.put("/update/{task_id}", status_code=status.HTTP_200_OK)
def update_task(task_id: int, body: TaskSchema, db: Session = Depends(get_db), user=Depends(is_authenticated)):
    return controller.update_task(task_id, body, db, user.id)


@task_routes.delete("/delete/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db), user=Depends(is_authenticated)):
    return controller.delete_task(task_id, db, user.id)


