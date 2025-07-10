from pydantic import BaseModel, EmailStr, ConfigDict

class CoachBase(BaseModel):
    nom: str
    specialite: str | None = None
    email: EmailStr

class CoachCreate(CoachBase):
    password: str

class CoachOut(CoachBase):
    id: int

class CoachLogin(BaseModel):
    email: EmailStr
    password: str

class CoachToken(BaseModel):
    access_token: str
    token_type: str

    model_config = ConfigDict(from_attributes=True)
