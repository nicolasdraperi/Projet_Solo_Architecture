from pydantic import BaseModel
from datetime import datetime

class SessionBase(BaseModel):
    dateHeure: datetime
    duree: int
    statut: str
    joueur_id: int
    coach_id: int

class SessionCreate(SessionBase):
    pass

class SessionOut(SessionBase):
    id: int

    class Config:
        orm_mode = True
