from pydantic import BaseModel

class UserRegister(BaseModel):
    user_name: str
    first_name: str
    last_name: str
    mobile_number: str
    email_id: str
    password: str    
    address: str
    city: str
    state: str
    contory: str


class UserLogin(BaseModel):
    user_name: str
    password: str

class Users(BaseModel): 
    reference_id : str   
    user_name: str
    user_id: str
    first_name: str
    last_name: str
    email_id: str
    password: str
    mobile_number: str
    address: str
    city: str
    state: str
    contory: str
    is_active: bool





    