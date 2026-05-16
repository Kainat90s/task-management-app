from pydantic import BaseModel
class UserSchema(BaseModel):
    name:str
    password:str
    is_User_Registered:bool=False
    
    
    
class UserSchemaResponse(BaseModel):  #post man mai jo response aey ga us mai sai sensitove fields hm 
    #skip karaingai takai user ka data expose na ho like password
    
   

    name:str

    is_User_Registered:bool