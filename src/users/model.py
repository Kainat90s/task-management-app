from src.utils.db import Base
from sqlalchemy import Column, String, Boolean, Integer
class User(Base):
    __tablename__= "Users"
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String, nullable=False)
    password=Column(String, nullable=False)
    is_User_Registered=Column(Boolean,default=False)