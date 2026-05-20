from src.utils.db import Base
from sqlalchemy import Column, String, Boolean, Integer, DateTime
class User(Base):
    __tablename__= "Users"
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String, nullable=False)
    username=Column(String,nullable=False)
    hash_password=Column(String, nullable=False)
    emaill=Column(String)
    is_User_Registered=Column(Boolean)