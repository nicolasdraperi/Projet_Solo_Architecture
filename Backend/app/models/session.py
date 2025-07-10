from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    dateHeure = Column(DateTime, nullable=False)
    duree = Column(Integer, nullable=False)
    statut = Column(String(50), nullable=False)
    
    joueur_id = Column(Integer, ForeignKey("joueurs.id"), nullable=False)
    coach_id = Column(Integer, ForeignKey("coachs.id"), nullable=False)
    
    paiement = relationship("Paiement", uselist=False, back_populates="session")
