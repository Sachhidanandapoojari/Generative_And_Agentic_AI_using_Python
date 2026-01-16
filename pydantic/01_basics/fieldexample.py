from pydantic import  BaseModel, Field
from typing import List, Dict, Optional


class Cart(BaseModel):
    user_id: int
    item: List[str]
    quantities: Dict[str, int] = Field(default_factory=dict)


class BlogPost(BaseModel):
    title: str
    content: str
    image_url : Optional[str] = None


# adding field to the data with validation
cart_details = {
    "user_id":123,
    "item":["Laptop","Mouse","Keyboard"],
    "quantities":{"laptop":1,"mouse":1,"keyboard":2}
}
cart_res=Cart(**cart_details)
print(cart_res)
