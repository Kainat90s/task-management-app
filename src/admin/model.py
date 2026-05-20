#first file
from sqlalchemy import Column, String, Integer, Boolean
from src.utils.db  import Base

class Admin(Base):
    
    __tablename__="AdminTable"
    id=Column(Integer, primary_key=True)
    name=Column(String)
    username=Column(String, nullable=True)
    hasd_password=Column(String, nullable=True)
    email=Column(String, nullable=True)
    
    