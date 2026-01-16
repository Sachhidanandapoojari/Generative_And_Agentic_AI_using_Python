from pydantic import BaseModel,field_validator,model_validator

class User(BaseModel):
    username:str
    
    @field_validator('username')
    def username_length(cls,v):
        if len(v)<4:
            raise ValueError("username must be least 4 char")
        return v

class SignupData(BaseModel):
    password:str
    conf_password:str
    
    @model_validator(mode='after')
    def password_match(self):
        if self.password!=self.conf_password:
            raise ValueError("Password do not match")
        return self
