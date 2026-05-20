from pydantic import BaseModel    #second file
class AdminSchema(BaseModel):
    name:str
    username:str
    password:str
    email:str
    
    
class AdminResponse(BaseModel):
    name:str
    username:str
    email:str
    
    
class AdminLoginShema(BaseModel):
      username:str
      password:str