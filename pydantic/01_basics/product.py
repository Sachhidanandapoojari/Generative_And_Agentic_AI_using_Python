from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name:str
    price:float
    in_stock:bool
product=Product(id=1,name="Books",price='200',in_stock="true")
print(product)