from pydantic import BaseModel
from datetime import datetime

class NotificationBase(BaseModel):
    message: str
    dateEnvoi: datetime
    joueur_id: int

class NotificationCreate(NotificationBase):
    pass

class NotificationOut(NotificationBase):
    id: int

    class Config:
        orm_mode = True
