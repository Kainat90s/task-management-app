# from src.users.dtos import UserSchema
# from sqlalchemy.orm import Session
# from src.users.model import User
# def create_user(body:UserSchema, db=Session):
#     data=body.model_dump()
#     new_data=User(name=data["name"], password=data['password'], is_User_Registered=data["is_User_Registered"])
#     db.add(new_data)
#     db.commit()
#     db.refresh(new_data)
#     return {"status":"user has created successfully", "data":new_data}
    
    
    
# def get_user_data(db:Session):
#     user=db.query(User).all()
#     # return {"status":"data accessed","data":user}
#     return user
# # def get_specific_id(user_id,db:session):
# #    user=db.query(User).filter(User.id==user_id)
# #    return {"status":"query accessed","data":user}
            
# def get_specific_id(user_id: int, db:Session):

#     user = db.query(User).filter(User.id == user_id).first()

#     if not user:
#         return {
#             "status": "user not found"
#         }
        
#     # if not user:
#     #     raise HTTPException(
#     #         status_code=404,
#     #         detail="User not found"
#     #     )

#     return user
    
    
# # def user_update(user_id:int,body:UserSchema, db:Session):
# #     user=db.get(User,user_id)
# #     if not user:
# #         return {"status":"user not found"}
# #     user.name=body.name
# #     user.password=body.password
# #     db.commit()
# #     db.refresh(user)
# #     return {"status":user}
    
    
# # from sqlalchemy.orm import Session
# # from fastapi import HTTPException
# # from src.users.model import User

# # def user_update(user_id: int, body:UserSchema, db: Session):

# #     user = db.get(User, user_id)

# #     if not user:
# #         raise HTTPException(
# #             status_code=404,
# #             detail="User not found"
# #         )

# #     # user.name = body.name
# #     # user.password = body.password
# #     # db.add(user)

# #     # db.commit()
# #     # db.refresh(user)
# #     body=body.model_dump()
# #     for key,val in body.items():
# #         setattr(user,key,val)

# #     return {
# #         "status": "User Updated Successfully",
# #         "data": user
# #     }
    
    
# from sqlalchemy.orm import Session
# from fastapi import HTTPException
# from src.users.model import User
# from src.users.dtos import UserSchema #isko get mai use kro takai hr sensitive data na jaey api ko

# def user_update(user_id: int, body: UserSchema, db: Session):

#     user = db.get(User, user_id)

#     if not user:
#         raise HTTPException(
#             status_code=404,
#             detail="User not found"
#         )

#     body = body.model_dump(exclude_unset=True)

#     for key, val in body.items():
#         setattr(user, key, val)
#     # db.add(user)

#     db.commit()
#     db.refresh(user)
#     return user

#     # return {
#     #     "status": "User Updated Successfully",
#     #     "data": user
#     # }
    
# def delete_user(user_id:int,db:Session):
#         user=db.get(User,user_id)
#         if not user:
#             return {"status":"user not found to delete"}
        
#         db.delete(user)
#         db.commit()
#         # db.refresh(user)
#         return None
        
        
from src.users.dtos import UserSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException, BackgroundTasks
from src.users.model import User
from pwdlib import PasswordHash
from src.utils.mail import send_email
hashPassword = PasswordHash.recommended()


async def create_user(body: UserSchema, db: Session ,bg_task:BackgroundTasks):
    
    # Email already exists check
    existing_email = db.query(User).filter(User.email == body.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already exists")
    
    # Username already exists check
    existing_username = db.query(User).filter(User.username == body.username).first()
    if existing_username:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    # Password hash karo
    hashed = hashPassword.hash(body.password)
    
    new_user = User(
        name=body.name,
        username=body.username,
        email=body.email,
        hash_password=hashed,
        is_User_Registered=body.is_User_Registered
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    res=await send_email([new_user.email])
    bg_task.add_task(send_email,[new_user.email])
  
    return new_user
   


def get_user_data(db: Session):
    users = db.query(User).all()
    return users


def get_specific_id(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user


def user_update(user_id: int, body: UserSchema, db: Session):
    user = db.get(User, user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Agar password update ho raha hai toh hash karo
    data = body.model_dump(exclude_unset=True)
    if "password" in data:
        data["hash_password"] = hashPassword.hash(data.pop("password"))
    
    for key, val in data.items():
        setattr(user, key, val)
    
    db.commit()
    db.refresh(user)
    return user


def delete_user(user_id: int, db: Session):
    user = db.get(User, user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    return None



from src.users.dtos import UserSchema, UserLoginSchema
from datetime import datetime, timedelta, timezone
import jwt
from src.utils.settings import settings

def user_login(body: UserLoginSchema, db: Session):
    
    # User dhundo
    user = db.query(User).filter(User.username == body.username).first()
    
    if not user:
        raise HTTPException(status_code=401, detail="Username not found")
    
    # Password verify karo
    if not hashPassword.verify(body.password, user.hash_password):
        raise HTTPException(status_code=401, detail="Invalid password")
    
    # Token banao
    exp_time = datetime.now(timezone.utc) + timedelta(minutes=settings.EXP)
    
    token = jwt.encode(
        {
            "id": user.id,
            "exp": exp_time
        },
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    
    return {"token": token}