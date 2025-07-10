from pydantic import BaseModel, EmailStr

class JoueurBase(BaseModel):
    nom: str
    email: EmailStr

class JoueurCreate(JoueurBase):
    password: str

class JoueurOut(JoueurBase):
    id: int

    class Config:
        orm_mode = True
