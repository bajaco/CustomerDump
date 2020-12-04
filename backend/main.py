from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

from . import ops, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
async def root():
    return {'message': 'Hallo'}

@app.post('/users/', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return ops.create_user(db=db, user=user)

@app.get('/users/', response_model=List[schemas.User])
def read_users(skip: int=0, limit: int=10, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users
