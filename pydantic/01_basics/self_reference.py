from pydantic import BaseModel
from typing import List,Optional
class Comment(BaseModel):
    id:int
    content:str
    replies:Optional[List['Comment']]=None
Comment.model_rebuild()

comment_res=Comment(
    id=111,
    content="Hey this is sk",
    replies=[
        Comment(id=222,content="this is inside 222",replies=[
            Comment(id=333,content="this is inside 333")
        ])
    ]
)
print(comment_res)
# print(comment_res.model_dump())


