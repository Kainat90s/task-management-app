
# from src.utils.db import get_db
# from src.admin.dtos import AdminResponse,AdminSchema,AdminLoginShema
# from fastapi import APIRouter,status, Depends, Request
# from src.admin import controller


# admin_routes=APIRouter(prefix='/admin')
# @admin_routes.post('/register',response_model=AdminResponse,status_code=status.HTTP_201_CREATED)
# def AdminRegister(body:AdminSchema,db=Depends(get_db)):
#     return controller.AdminRegister(body,db)

# @admin_routes.post('/login', status_code=status.HTTP_200_OK)
# def AdminLogin(body:AdminLoginShema, db=Depends(get_db)):
#   return controller.AdminLogin(body,db)
# @admin_routes.get('/isAuth', status_code=status.HTTP_200_OK)
# def isAuth(request:Request, db=Depends(get_db)):
#   return controller.is_authenticated(request,db)

from fastapi import APIRouter, Depends, status, Request
from src.admin.model import Admin
from src.utils.hepers import is_authenticated
from src.utils.db import get_db
from src.admin.dtos import (
    AdminResponse,
    AdminSchema,
    AdminLoginShema
)
from src.admin import controller

admin_routes = APIRouter(prefix="/admin")


@admin_routes.post(
    "/register",
    response_model=AdminResponse,
    status_code=status.HTTP_201_CREATED
)
def AdminRegister(body: AdminSchema, db=Depends(get_db), user=Depends(is_authenticated)):
    return controller.AdminRegister(body, db)


@admin_routes.post(
    "/login",
    status_code=status.HTTP_200_OK
)
def AdminLogin(body: AdminLoginShema, db=Depends(get_db)):
    return controller.AdminLogin(body, db)



@admin_routes.get(
    "/all_admins",
    status_code=status.HTTP_200_OK
)
def all_admins(db=Depends(get_db), user=Depends(is_authenticated)):
    return controller.GetAllAdmins(db)


@admin_routes.delete(
    "/delete/{id}",
    status_code=status.HTTP_200_OK
)
def delete_admin(id: int, db=Depends(get_db), user=Depends(is_authenticated)):
    return controller.DeleteAdmin(id, db)


@admin_routes.put(
    "/update/{id}",
    status_code=status.HTTP_200_OK
)
def update_admin(id: int, body: AdminSchema, db=Depends(get_db), user=Depends(is_authenticated)):
    return controller.UpdateAdmin(id, body, db)

@admin_routes.get(
    "/isAuth",
    status_code=status.HTTP_200_OK
)
def isAuth(request: Request, db=Depends(get_db)):
    return controller.is_authenticated(request, db)
    