from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Paiement(Base):
    __tablename__ = "paiements"

    id = Column(Integer, primary_key=True, index=True)
    montant = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False)
    statut = Column(String(50), nullable=False)
    session_id = Column(Integer, ForeignKey("sessions.id"), nullable=False)

    session = relationship("Session", back_populates="paiement")
