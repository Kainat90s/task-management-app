# SQLAlchemy ke required columns aur datatypes import
from sqlalchemy import Column, Integer, String, Boolean

# Base class import
from src.utils.db import Base


# Task model ban raha hai
class Task(Base):

    # Database table ka naam
    __tablename__ = "tasks"

    # Task ki unique ID
    id = Column(Integer, primary_key=True, index=True)

    # Task ka title
    title = Column(String, nullable=False)

    # Task ki description
    description = Column(String, nullable=True)

    # Task complete hui ya nahi
    is_completed = Column(Boolean, default=False)