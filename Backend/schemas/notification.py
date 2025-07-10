from pydantic import BaseModel, ConfigDict
from datetime import datetime

class NotificationBase(BaseModel):
    message: str
    dateEnvoi: datetime
    joueur_id: int

class NotificationCreate(NotificationBase):
    pass

class NotificationOut(NotificationBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
