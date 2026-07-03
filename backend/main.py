from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse
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
    climb_type = Column(String, default="Boulder") # new field

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bouldering Tracker API with db PostgreSQL")

class ClimbCreate(BaseModel):
    route_name: str
    grade: str
    style: str
    location: str
    climb_type: str = "Boulder"

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

# New endpoint: delete entry
@app.delete("/api/climbs/{climb_id}")
def delete_climb(climb_id: int, db: Session = Depends(get_db)):
    climb = db.query(ClimbDB).filter(ClimbDB.id == climb_id).first()
    if climb:
        db.delete(climb)
        db.commit()
        return {"status": "ok"}
    return {"status": "not found"}

@app.get("/health")
def health_check():
    return {"status": "ok", "database": "connected"}

@app.get("/")
def serve_frontend():
    """Serving main graphic interface"""
    return FileResponse("index.html")