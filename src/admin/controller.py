# from src.admin.dtos import AdminResponse, AdminSchema
# from sqlalchemy.orm import Session
# from src.admin.model import Admin
# from pwdlib import PasswordHash
# from fastapi import HTTPException,status
# from src.admin.dtos import AdminLoginShema
# import jwt

# password_hash = PasswordHash.recommended()


# def get_hash(password):
#     return password_hash.hash(password)

# def verifyPassword(plan_password,hashed_password):
#     return password_hash.hash(plan_password,hashed_password)


# def AdminRegister(body: AdminSchema, db: Session):

#     is_admin_name = db.query(Admin).filter(
#         Admin.username == body.username
#     ).first()

#     is_admin_email = db.query(Admin).filter(
#         Admin.email == body.email
#     ).first()

#     if is_admin_name:
#         raise HTTPException(
#             status_code=400,
#             detail="duplicated username"
#         )

#     if is_admin_email:
#         raise HTTPException(
#             status_code=400,
#             detail="duplicated email"
#         )

#     maira_hash_password = get_hash(body.password)

#     user = Admin(
#         name=body.name,
#         username=body.username,
#         hasd_password=maira_hash_password,
#         email=body.email
#     )

#     db.add(user)
#     db.commit()
#     db.refresh(user)

#     return user

# def AdminLogin(body:AdminLoginShema, db:Session):
  
#     is_admin_name = db.query(Admin).filter(
#         Admin.username == body.username
#     ).first()

    

#     if not is_admin_name:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED400,
#             detail="you entered wrong user name"
#         )

#     if not verifyPassword(body.password,Admin.hasd_password):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED400,
#             detail="you enterd wrong password"
#         )
        
    
     
         
# from datetime import datetime, timedelta
# from fastapi import HTTPException, status
# from sqlalchemy.orm import Session
# from src.admin.model import Admin
# from src.admin.dtos import (
#     AdminSchema,
#     AdminLoginShema
# )
# from pwdlib import PasswordHash
# from src.utils.settings import settings
# import jwt


# password_hash = PasswordHash.recommended()


# # =========================
# # HASH PASSWORD
# # =========================

# def get_hash(password):
#     return password_hash.hash(password)


# # =========================
# # VERIFY PASSWORD
# # =========================

# def verify_password(plain_password, hashed_password):
#     return password_hash.verify(
#         plain_password,
#         hashed_password
#     )


# # =========================
# # ADMIN REGISTER
# # =========================

# def AdminRegister(body: AdminSchema, db: Session):

#     user_name = db.query(Admin).filter(
#         Admin.username == body.username
#     ).first()

#     user_email = db.query(Admin).filter(
#         Admin.email == body.email
#     ).first()

#     if user_name:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="duplicated username"
#         )

#     if user_email:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="duplicated email"
#         )

#     hash_password = get_hash(
#         body.password
#     )

#     user = Admin(
#         name=body.name,
#         username=body.username,
#         hasd_password=hash_password,
#         email=body.email
#     )

#     db.add(user)
#     db.commit()
#     db.refresh(user)

#     return {
#         "message": "admin registered successfully"
#     }


# # =========================
# # ADMIN LOGIN
# # =========================

# def AdminLogin(body: AdminLoginShema, db: Session):

#     user = db.query(Admin).filter(
#         Admin.username == body.username
#     ).first()

#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="you entered wrong username"
#         )

#     if not verify_password(
#         body.password,
#         user.hasd_password
#     ):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="you entered wrong password"
#         )

#     exp_time = datetime.now() + timedelta(
#         minutes=settings.EXP
#     )

#     token = jwt.encode(
#         {
#             "_id": user.id,
#             "exp": exp_time
#         },
#         settings.SECRET_KEY,
#         algorithm=settings.ALGORITHM
#     )

#     return {
#         "token": token
#     }


# from src.admin.dtos import AdminSchema,AdminLoginShema
# from src.admin.model import Admin
# from sqlalchemy.orm import Session
# from fastapi import Depends, status,HTTPException,Request
# from pwdlib import PasswordHash
# from datetime import datetime , timedelta
# from src.utils import settings
# from src.utils.settings import settings
# import jwt
# from jwt import InvalidTokenError
# hashPassword=PasswordHash.recommended()

# def converPasswordHash(password):
#     return hashPassword.hash(password)


# def AdminRegister(body:AdminSchema, db:Session):
#         userEmail=db.query(Admin).filter(Admin.email==body.email).first()
#         userName=db.query(Admin).filter(Admin.username==body.username).first()
#         if  userEmail:
#             raise HTTPException(status_code=401,  detail="duplicated email found")
        
#         if  userName:
#             raise HTTPException(status_code=401,  detail="duplicated username found")
#         BodyPassword=converPasswordHash(body.password)
        
#         user=Admin(
#             name=body.name,
#             username=body.username,
#             hasd_password=BodyPassword,
#             email=body.email
#         )
#         db.add(user)
#         db.commit()
#         db.refresh(user)
        
#         return  user
# def verifyPassword(plainPassword,hashedPassword):
#  return hashPassword.verify(plainPassword,hashedPassword)



# def AdminLogin(body:AdminLoginShema,db:Session):
#   user=db.query(Admin).filter(Admin.username==body.username).first()
   
#   if not user:
#      raise HTTPException(status_code=401,  detail=" email not found")
 
#   if not verifyPassword(body.password,user.hasd_password):
#      raise HTTPException(status_code=401,  detail=" password not found")
 
#   exp_time=datetime.now()+timedelta(minutes=settings.EXP)
#   token=jwt.encode({"id":user.id,"exp":exp_time},settings.SECRET_KEY,settings.ALGORITHM)
#   return {"token":token}

# from fastapi import HTTPException, status, Request
# from sqlalchemy.orm import Session
# import jwt
# from jwt.exceptions import InvalidTokenError

# def is_authenticated(request: Request, db: Session):
#     token = request.headers.get("authorization")
#     if not token:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized.")

#     token = token.split(" ")[-1]

#     data = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
#     user_id = data.get("id")
#     exp_time = int(data.get("exp"))
    

#     current_time = datetime.now().timestamp()
#     print(exp_time - current_time)

#     if current_time > exp_time:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized 2dlast.")

#     user = db.query(Admin).filter(Admin.id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized last.")

#     return user




from src.admin.dtos import AdminSchema, AdminLoginShema
from src.admin.model import Admin
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Request
from pwdlib import PasswordHash
from datetime import datetime, timedelta
from src.utils.settings import settings
import jwt
from datetime import datetime, timedelta, timezone
hashPassword = PasswordHash.recommended()


def converPasswordHash(password):
    return hashPassword.hash(password)


def verifyPassword(plainPassword, hashedPassword):
    return hashPassword.verify(plainPassword, hashedPassword)


def AdminRegister(body: AdminSchema, db: Session):

    userEmail = db.query(Admin).filter(Admin.email == body.email).first()
    if userEmail:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

    userName = db.query(Admin).filter(Admin.username == body.username).first()
    if userName:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )

    user = Admin(
        name=body.name,
        username=body.username,
        email=body.email,
        hasd_password=converPasswordHash(body.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def GetAllAdmins(db: Session):
    users = db.query(Admin).all()
    return users


def DeleteAdmin(id: int, db: Session):
    user = db.query(Admin).filter(Admin.id == id).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    db.delete(user)
    db.commit()
    return {"message": "Admin deleted successfully"}



def UpdateAdmin(id: int, body: AdminSchema, db: Session):
    user = db.query(Admin).filter(Admin.id == id).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    user.name = body.name
    user.username = body.username
    user.email = body.email
    
    db.commit()
    db.refresh(user)
    return user



def AdminLogin(body: AdminLoginShema, db: Session):

    user = db.query(Admin).filter(
        Admin.username == body.username
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username not found"
        )

    if not verifyPassword(body.password, user.hasd_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid password"
        )

    # exp_time = datetime.utcnow() + timedelta(
    #     minutes=settings.EXP
    # )
    
    exp_time = datetime.now(timezone.utc) + timedelta(minutes=30)
    print("Token expire hoga:", exp_time)
    print("Abhi time hai:", datetime.now(timezone.utc))

    token = jwt.encode(
        {
            "id": user.id,
            "exp": exp_time
        },
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return {
        "token": token
    }


def is_authenticated(request: Request, db: Session):

    auth_header = request.headers.get("Authorization")

    if not auth_header:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header missing"
        )

    try:
        token = auth_header.split(" ")[1]

        data = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        print(data)

        user_id = data.get("id")

        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )

        user = db.query(Admin).filter(
            Admin.id == user_id
        ).first()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found"
            )

        return user

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired"
        )

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )