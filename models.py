from sqlalchemy import Column, ForeignKey,Integer,String
from database import Base
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer,primary_key=True,index=True)
    title=Column(String)
    body=Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    creation = relationship("User", back_populates="creator")

    
class User(Base):
    __tablename__ ='users'
    id = Column(Integer,primary_key=True,index=True)
    name=Column(String,unique=True)
    email=Column(String) 
    password = Column(String)
    
    creator = relationship("Blog", back_populates="creation")
    
    
    
    
    
    
    
