from fastapi import APIRouter,Depends,status
from src.users.dtos import UserSchema,UserSchemaResponse
from src.users import controller
from src.utils.db import get_db
from typing import List
from sqlalchemy.orm import Session

user_routes= APIRouter(prefix="/user")
@user_routes.post("/create", status_code=status.HTTP_201_CREATED)  #for creation successfully
def create_user(body:UserSchema, db=Depends(get_db)):
    return controller.create_user(body,db)

@user_routes.get('/get_user',response_model=List[UserSchemaResponse],status_code=status.HTTP_200_OK)# for fetcching data successfully
def get_user_data(db:Session=Depends(get_db)):
    return controller.get_user_data(db)


@user_routes.get("/get_user/{user_id}",response_model=UserSchemaResponse,status_code=status.HTTP_200_OK)
def get_specific_id(user_id,db:Session=Depends(get_db)):
    return controller.get_specific_id(user_id,db)



    
@user_routes.put("/update/{user_id}",response_model=UserSchemaResponse,status_code=status.HTTP_201_CREATED)
def user_update(
    user_id: int,
    body: UserSchema,
    db:Session=Depends(get_db)
):
    return controller.user_update(user_id, body, db)
@user_routes.delete('/delete/{user_id}',response_model=None,status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id:int,db:Session=Depends(get_db)):
    # return controller.delete_user(user_id,db)
    return controller.delete_user(user_id,db)