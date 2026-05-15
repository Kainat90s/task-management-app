from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import session
from src.tasks.model import Task
def create_task(body:TaskSchema, db:session):
  data=body.model_dump()
  new_data=Task(title=data["title"], description=data["description"], is_completed=data["is_completed"])
  db.add(new_data)
  db.commit()
  db.refresh(new_data)
  print(body.model_dump())
    
  return {"status":"task has created successfully", "data":new_data}