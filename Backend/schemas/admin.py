from pydantic import BaseModel, EmailStr, ConfigDict

class AdminBase(BaseModel):
    nom: str
    email: EmailStr

class AdminCreate(AdminBase):
    password: str

class AdminOut(AdminBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
