from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root(db: Session = Depends(get_db)):
    return {"message": "DB connection OK"}
