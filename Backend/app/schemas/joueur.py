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

class JoueurLogin(BaseModel):
    email: EmailStr
    password: str

class JoueurToken(BaseModel):
    access_token: str
    token_type: str = "bearer"
