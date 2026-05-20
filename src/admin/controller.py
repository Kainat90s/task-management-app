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
        
    
     
         
from datetime import datetime, timedelta
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.admin.model import Admin
from src.admin.dtos import (
    AdminSchema,
    AdminLoginShema
)
from pwdlib import PasswordHash
from src.utils.settings import settings
import jwt


password_hash = PasswordHash.recommended()


# =========================
# HASH PASSWORD
# =========================

def get_hash(password):
    return password_hash.hash(password)


# =========================
# VERIFY PASSWORD
# =========================

def verify_password(plain_password, hashed_password):
    return password_hash.verify(
        plain_password,
        hashed_password
    )


# =========================
# ADMIN REGISTER
# =========================

def AdminRegister(body: AdminSchema, db: Session):

    user_name = db.query(Admin).filter(
        Admin.username == body.username
    ).first()

    user_email = db.query(Admin).filter(
        Admin.email == body.email
    ).first()

    if user_name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="duplicated username"
        )

    if user_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="duplicated email"
        )

    hash_password = get_hash(
        body.password
    )

    user = Admin(
        name=body.name,
        username=body.username,
        hasd_password=hash_password,
        email=body.email
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "message": "admin registered successfully"
    }


# =========================
# ADMIN LOGIN
# =========================

def AdminLogin(body: AdminLoginShema, db: Session):

    user = db.query(Admin).filter(
        Admin.username == body.username
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="you entered wrong username"
        )

    if not verify_password(
        body.password,
        user.hasd_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="you entered wrong password"
        )

    exp_time = datetime.now() + timedelta(
        minutes=settings.EXP
    )

    token = jwt.encode(
        {
            "_id": Admin.id,
            "exp": exp_time
        },
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return {
        "token": token
    }