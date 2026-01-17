from pydantic import BaseModel,ConfigDict
from datetime import datetime
from typing import List

class Address(BaseModel):
    street:str
    city:str
    postal_code:str
    
class User(BaseModel):
    id:int
    name:str
    email:str
    is_active:bool=True
    address:Address
    created_at:datetime
    tags:List[str]=[]
    
model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S")
        }
    )
user=User(
    id=1,
    name="Sachin",
    email="sac@gmail.com",
    address=Address(
        street="MG Road",
        city="Bangalore",
        postal_code="560001"
    ),
    created_at=datetime.now(),
    tags=["admin","developer"] 
)

print(user.model_dump_json())