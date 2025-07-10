from sqlalchemy import Column, Integer, String
from app.core.database import Base
from sqlalchemy.orm import relationship

class Joueur(Base):
    __tablename__ = "joueurs"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(128), nullable=False)



notifications = relationship("Notification", back_populates="joueur")
