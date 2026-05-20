
from src.utils.db import get_db
from src.admin.dtos import AdminResponse,AdminSchema,AdminLoginShema
from fastapi import APIRouter,status, Depends
from src.admin import controller


admin_routes=APIRouter(prefix='/admin')
@admin_routes.post('/register',response_model=AdminResponse,status_code=status.HTTP_201_CREATED)
def AdminRegister(body:AdminSchema,db=Depends(get_db)):
    return controller.AdminRegister(body,db)

@admin_routes.post('/login', status_code=status.HTTP_200_OK)
def AdminLogin(body:AdminLoginShema, db=Depends(get_db)):
  return controller.AdminLogin(body,db)