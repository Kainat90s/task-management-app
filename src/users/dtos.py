from pydantic import BaseModel
class UserSchema(BaseModel):
    name:str
    password:str
    is_User_Registered:bool=False