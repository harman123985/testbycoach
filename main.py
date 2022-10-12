from typing import List
from fastapi import FastAPI,Depends,status,Response,HTTPException

import schemas,models
from database import SessionLocal, engine
from sqlalchemy.orm  import Session
from hashing import Hash
app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.post('/blog')
# def create(title,body):
#     return {'title':title,'body':body}

@app.post('/blog',status_code=status.HTTP_201_CREATED,tags=['blogs'])
def create (request : schemas.BlogSchema,db:Session = Depends(get_db)):
    new_blog= models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog 

# @app.get('/blog',status_code=200,tags=['blogs'])
# def all (db:Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

@app.get('/blogid',response_model=schemas.BlogSchema,tags=['blogs'])
def get_one (Id:int,response:Response,db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id==Id).first()
    if not blogs:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'datail':'no found'}
    db.commit()
    return blogs

@app.put('/blog',tags=['blogs'])
def update(Id:int,response:Response,request : schemas.BlogSchema,db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id==Id).first()
    if not blogs:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'detail':'not found'}
    blogs.title=request.title
    blogs.body=request.body
    
    db.commit()
    return {"Updated"}

@app.delete('/blog',tags=['blogs'])
def delete (Id:int,response:Response,db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id==Id).first()
    if not blogs:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'detail':'not found'}
    db.delete(blogs)
    db.commit()
    return {'deleted succesfully'}

@app.post('/user',status_code=status.HTTP_201_CREATED ,tags=['Users'])
def create(request:schemas.UserSchema,db:Session=Depends(get_db)):
    new_user= models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get('/user',response_model=schemas.UserSchemaGet,tags=['Users'])
def getall (db:Session = Depends(get_db)):
    users = db.query(models.User).all() 
    return users

@app.get('/blogs',response_model=schemas.BlogSchemaGet,tags=['Users'])
def getblog (Id:int,response:Response,db:Session = Depends(get_db)):
    users = db.query(models.Blog).filter(models.User.id==Id).first()
    if not users:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'detail':'not found'}    
    return users
















