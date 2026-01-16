from pydantic import field_validator,BaseModel,model_validator
from datetime import datetime

class Person(BaseModel):  
    first_name:str
    last_name:str
    
    field_validator('first_name', 'last_name')
    def name_must_be_capitalized(cls, v: str):
        if not v.istitle():
            raise ValueError('Name must be capitalized')
        return v

class User(BaseModel):
    email:str
    @field_validator('email')
    def normalize_email(cls,v: str):
        return v.lower().strip()
    
class Product(BaseModel):
    price:float
    
    @field_validator('price',mode='before')
    def parse_price(cls,v:str):
        if v.isinstance(v,str):
            return float(v.replace('$',''))
        return v
    
class DateRange(BaseModel):
    start_date:datetime
    end_date:datetime
    
    
    @model_validator(mode="after")
    def validate_date_range(self):
        if self.start_date>=self.end_date:
            raise ValueError("start_date must be before end_date")
        return self
dat_res=DateRange(
    start_date=datetime(2024, 1, 1),
    end_date=datetime(2024, 1, 5)
)      
print(dat_res) 


            
        
    