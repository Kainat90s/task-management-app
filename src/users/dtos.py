from pydantic import BaseModel

class UserSchema(BaseModel):
    name: str
    username: str
    password: str
    email: str
    is_User_Registered: bool = False

class UserSchemaResponse(BaseModel):
    id: int
    name: str
    username: str
    email: str
    is_User_Registered: bool

    class Config:
        from_attributes = True
        
        
class UserLoginSchema(BaseModel):
    username: str
    password: str
    