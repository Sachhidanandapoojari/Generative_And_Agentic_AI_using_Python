from pydantic import BaseModel
from typing import List,Optional
class Address(BaseModel):
    street:str
    city:str
    postal_code:str

class User(BaseModel):
    id:int
    name:str
    address:Address

user_data = {
    "id":12,
    "name":"sachin",
    "address":{
        "street":"Ram",
        "city":"Mysore",
        "postal_code":"ABC",
    }
    
}

user_res=User(**user_data)
print(user_res)
    
    
    