from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from typing import List

DATABASE_URL = "postgresql://bouldering_user:supersecretpassword@postgres-service:5432/bouldering_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class ClimbDB(Base):
    __tablename__ = "climbs"
    id = Column(Integer, primary_key=True, index=True)
    route_name = Column(String, index=True)
    grade = Column(String)
    style = Column(String)
    location = Column(String)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bouldering Tracker API with db PostgreSQL")

class ClimbCreate(BaseModel):
    route_name: str
    grade: str
    style: str
    location: str

class ClimbResponse(ClimbCreate):
    id: int
    class Config:
        from_attributes = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/climbs", response_model=List[ClimbResponse])
def get_climbs(db: Session = Depends(get_db)):
    """Returns all completed climbs from PostgreSQL"""
    return db.query(ClimbDB).all()

@app.post("/api/climbs", response_model=ClimbResponse)
def add_climb(climb: ClimbCreate, db: Session = Depends(get_db)):
    """Permanent save for new climb"""
    new_climb = ClimbDB(**climb.model_dump())
    db.add(new_climb)
    db.commit()
    db.refresh(new_climb)
    return new_climb

@app.get("/health")
def health_check():
    return {"status": "ok", "database": "connected"}