# from src.tasks.dtos import TaskSchema
# from sqlalchemy.orm import session
# from src.tasks.model import Task
# def create_task(body:TaskSchema, db:session):
#   data=body.model_dump()
#   new_data=Task(title=data["title"], description=data["description"], is_completed=data["is_completed"])
#   db.add(new_data)
#   db.commit()
#   db.refresh(new_data)
#   print(body.model_dump())
    
#   return {"status":"task has created successfully", "data":new_data}

from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.tasks.model import Task


def create_task(body: TaskSchema, db: Session, user_id: int):
    data = body.model_dump()
    
    new_task = Task(
        title=data["title"],
        description=data["description"],
        is_completed=data["is_completed"],
        user_id=user_id  # 👈 token se aaya
    )
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    return new_task


def get_user_tasks(db: Session, user_id: int):
    # Sirf usi user ke tasks dikhao
    tasks = db.query(Task).filter(Task.user_id == user_id).all()
    return tasks


def get_specific_task(task_id: int, db: Session, user_id: int):
    task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user_id  # 👈 sirf apna task access kare
    ).first()
    
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    
    return task


def update_task(task_id: int, body: TaskSchema, db: Session, user_id: int):
    task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user_id  # 👈 sirf apna task update kare
    ).first()
    
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found or not yours"
        )
    
    data = body.model_dump(exclude_unset=True)
    for key, val in data.items():
        setattr(task, key, val)
    
    db.commit()
    db.refresh(task)
    return task


def delete_task(task_id: int, db: Session, user_id: int):
    task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user_id  # 👈 sirf apna task delete kare
    ).first()
    
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found or not yours"
        )
    
    db.delete(task)
    db.commit()
    return None

def get_all_tasks(db: Session):
    tasks = db.query(Task).all()
    return tasks