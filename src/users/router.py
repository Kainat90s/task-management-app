from fastapi import APIRouter,Depends
from src.users.dtos import UserSchema
from src.users import controller
from src.utils.db import get_db

user_routes= APIRouter(prefix="/user")
@user_routes.post("/create")
def create_user(body:UserSchema, db=Depends(get_db)):
    return controller.create_user(body,db)

@user_routes.get('/get_user')
def get_user_data(db=Depends(get_db)):
    return controller.get_user_data(db)