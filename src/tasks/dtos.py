# Pydantic BaseModel import
from pydantic import BaseModel


# Task create karne ka DTO/schema
class TaskSchema(BaseModel):

    # Task ka title
    title: str

    # Task ki description
    description: str
    is_completed: bool=False

# Task response DTO/schema
# class TaskResponseDTO(BaseModel):

#     # Task ki ID
#     id: int

#     # Task ka title
#     title: str

#     # Task ki description
#     description: str

#     # Task completed hai ya nahi
#     is_completed: bool=False


#     # SQLAlchemy model ko response mein convert karne ke liye
#     class Config:
#         from_attributes = True