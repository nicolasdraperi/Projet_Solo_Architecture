from pydantic import BaseModel
from datetime import datetime

class PaiementBase(BaseModel):
    montant: float
    date: datetime
    statut: str
    session_id: int

class PaiementCreate(BaseModel):
    session_id: int
    montant: float

class PaiementOut(PaiementBase):
    id: int

    class Config:
        orm_mode = True
