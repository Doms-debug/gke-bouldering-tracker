from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Bouldering Tracker API")


class Climb(BaseModel):
    route_name: str
    grade: str
    style: str  # OS, Flash, RP
    location: str

climbs_db = [
    {"route_name": "Biała Rysa", "grade": "6A", "style": "OS", "location": "Jura"},
    {"route_name": "Panelowy Klasyk", "grade": "6B", "style": "Flash", "location": "Murall Warszawa"}
]

@app.get("/api/climbs", response_model=List[Climb])
def get_climbs():
    """Return list of all completed climbs"""
    return climbs_db

@app.post("/api/climbs")
def add_climb(climb: Climb):
    """Add to base"""
    climbs_db.append(climb.model_dump())
    return {"message": "Route succesfully saved!", "climb": climb}

@app.get("/health")
def health_check():
    """Kuberenetes endpoint liveness"""
    return {"status": "ok"}