from src.users.dtos import UserSchema
from sqlalchemy.orm import session
from src.users.model import User
def create_user(body:UserSchema, db=session):
    data=body.model_dump()
    new_data=User(name=data["name"], password=data['password'], is_User_Registered=data["is_User_Registered"])
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return {"status":"user has created successfully", "data":new_data}
    
    
    
def get_user_data(db:session):
    user=db.query(User).all()
    return {"status":"data accessed","data":user}
    
    
    
    