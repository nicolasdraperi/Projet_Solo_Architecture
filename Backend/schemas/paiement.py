from pydantic import BaseModel, ConfigDict
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

    model_config = ConfigDict(from_attributes=True)
