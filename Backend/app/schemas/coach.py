from pydantic import BaseModel, EmailStr

class CoachBase(BaseModel):
    nom: str
    specialite: str | None = None
    email: EmailStr

class CoachCreate(CoachBase):
    password: str

class CoachOut(CoachBase):
    id: int

    class Config:
        orm_mode = True
