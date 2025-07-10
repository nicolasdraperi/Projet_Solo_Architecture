from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class SessionBase(BaseModel):
    date_heure: datetime
    duree_minutes: int
    prix: float

class SessionCreate(BaseModel):
    date_heure: datetime
    duree_minutes: int
    prix: float

class SessionUpdate(BaseModel):
    date_heure: datetime
    duree_minutes: int
    prix: float

class SessionOut(SessionBase):
    id: int
    statut: str
    joueur_id: Optional[int]
    coach_id: int

    model_config = ConfigDict(from_attributes=True)
