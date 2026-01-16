from pydantic import BaseModel

class User(BaseModel):
    name:str
    age:int
    is_active:bool
user_val={'name':'sachin','age':25,'is_active':True}
res=User(**user_val)
print(res)

