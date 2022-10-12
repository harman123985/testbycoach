from typing import List,Optional
from pydantic import BaseModel

class BlogSchema (BaseModel):
    title : str
    body : str

    class Config():
        orm_mode = True

class UserSchema(BaseModel):
    name : str
    email : str
    password :str
   
    class Config():
        orm_mode = True
        
class UserSchemaGet(BaseModel):
    id : int
    name : str
    email : str
    password :str
    creator :BlogSchema 
   
    class Config():
        orm_mode = True
        
class BlogSchemaGet (BaseModel):
    id : int
    title : str
    body : str
    creation : UserSchema

    class Config():
        orm_mode = True
                
# class UserSchema(BaseModel):
#     name : str
#     email : str
#     password :str
   
#     class Config():
#         orm_mode = True
        
# class ShowUser(BaseModel):
#     name :str
#     email : str
#     creation : list[Blog] = []
    
#     class Config():
#         orm_mode = True

# class ShowBlog(BaseModel):
#     title :str
#     body : str
#     creation : list=[]
    
#     class Config():
#         orm_mode = True 
        
# class ShowUser(BaseModel):
#     name :str
#     email : str
#     creator : List=[]
    
#     class Config():
#         orm_mode = True
        
