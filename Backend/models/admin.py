from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(128), nullable=False)
