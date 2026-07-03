# # SQLAlchemy ke required columns aur datatypes import
# from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

# # Base class import
# from src.utils.db import Base


# # Task model ban raha hai
# class Task(Base):

#     # Database table ka naam
#     __tablename__ = "tasks"

#     # Task ki unique ID
#     id = Column(Integer, primary_key=True, index=True)

#     # Task ka title
#     title = Column(String, nullable=False)

#     # Task ki description
#     description = Column(String, nullable=True)

#     # Task complete hui ya nahi
#     is_completed = Column(Boolean, default=False)
#     user_id=Column(Integer, ForeignKey("AdminTable.id",  ondelete='CASCADE'))  #cascade connected task

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from src.utils.db import Base
# class Task(Base):
#     __tablename__ = "tasks"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, nullable=False)
#     description = Column(String, nullable=True)
#     is_completed = Column(Boolean, default=False)
    
#     # Admin ki jagah User se connect karo
#     user_id = Column(Integer, ForeignKey("Users.id", ondelete='CASCADE'))

from sqlalchemy.orm import relationship

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    is_completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("Users.id", ondelete='CASCADE'))
    
    user = relationship("User")  # 👈 yeh add karo