from pydantic import BaseModel
from datetime import datetime

class PaiementBase(BaseModel):
    montant: float
    date: datetime
    statut: str
    session_id: int

class PaiementCreate(PaiementBase):
    pass

class PaiementOut(PaiementBase):
    id: int

    class Config:
        orm_mode = True
