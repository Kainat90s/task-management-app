from pydantic import BaseModel

class UserSchema(BaseModel):
    name: str
    username: str
    password: str
    email: str
    is_User_Registered: bool
    
class UserSchemaResponse(BaseModel):
    id: int
    name: str
    username: str
    email: str
    is_User_Registered: bool
    