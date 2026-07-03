from src.utils.db import Base
from sqlalchemy import Column, Integer, String, Boolean  # 👈 yeh import karo

class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    hash_password = Column(String, nullable=False)
    email = Column(String)
    is_User_Registered = Column(Boolean)