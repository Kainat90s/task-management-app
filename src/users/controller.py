from src.users.dtos import UserSchema
from sqlalchemy.orm import Session
from src.users.model import User
def create_user(body:UserSchema, db=Session):
    data=body.model_dump()
    new_data=User(name=data["name"], password=data['password'], is_User_Registered=data["is_User_Registered"])
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return {"status":"user has created successfully", "data":new_data}
    
    
    
def get_user_data(db:Session):
    user=db.query(User).all()
    # return {"status":"data accessed","data":user}
    return user
# def get_specific_id(user_id,db:session):
#    user=db.query(User).filter(User.id==user_id)
#    return {"status":"query accessed","data":user}
            
def get_specific_id(user_id: int, db:Session):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return {
            "status": "user not found"
        }
        
    # if not user:
    #     raise HTTPException(
    #         status_code=404,
    #         detail="User not found"
    #     )

    return user
    
    
# def user_update(user_id:int,body:UserSchema, db:Session):
#     user=db.get(User,user_id)
#     if not user:
#         return {"status":"user not found"}
#     user.name=body.name
#     user.password=body.password
#     db.commit()
#     db.refresh(user)
#     return {"status":user}
    
    
# from sqlalchemy.orm import Session
# from fastapi import HTTPException
# from src.users.model import User

# def user_update(user_id: int, body:UserSchema, db: Session):

#     user = db.get(User, user_id)

#     if not user:
#         raise HTTPException(
#             status_code=404,
#             detail="User not found"
#         )

#     # user.name = body.name
#     # user.password = body.password
#     # db.add(user)

#     # db.commit()
#     # db.refresh(user)
#     body=body.model_dump()
#     for key,val in body.items():
#         setattr(user,key,val)

#     return {
#         "status": "User Updated Successfully",
#         "data": user
#     }
    
    
from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.users.model import User
from src.users.dtos import UserSchema #isko get mai use kro takai hr sensitive data na jaey api ko

def user_update(user_id: int, body: UserSchema, db: Session):

    user = db.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    body = body.model_dump(exclude_unset=True)

    for key, val in body.items():
        setattr(user, key, val)
    # db.add(user)

    db.commit()
    db.refresh(user)
    return user

    # return {
    #     "status": "User Updated Successfully",
    #     "data": user
    # }
    
def delete_user(user_id:int,db:Session):
        user=db.get(User,user_id)
        if not user:
            return {"status":"user not found to delete"}
        
        db.delete(user)
        db.commit()
        # db.refresh(user)
        return None
        