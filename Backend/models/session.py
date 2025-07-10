from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.core.database import Base

class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    date_heure = Column(DateTime, nullable=False)
    duree_minutes = Column(Integer, nullable=False)
    prix = Column(Float, nullable=False)
    statut = Column(String(20), default="disponible")
    joueur_id = Column(Integer, ForeignKey("joueurs.id"), nullable=True)
    coach_id = Column(Integer, ForeignKey("coachs.id"), nullable=False)

    
    paiement = relationship("Paiement", uselist=False, back_populates="session")
