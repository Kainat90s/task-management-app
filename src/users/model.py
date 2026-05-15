# SQLAlchemy ke required columns aur datatypes import
from sqlalchemy import Column, Integer, String

# Base class import
from src.utils.db import Base


# User model ban raha hai
class User(Base):

    # Database table ka naam
    __tablename__ = "users"

    # User ki unique ID
    id = Column(Integer, primary_key=True, index=True)

    # User ka name
    name = Column(String, nullable=False)

    # User ka email
    email = Column(String, unique=True, nullable=False)

    # User ka password
    password = Column(String, nullable=False)