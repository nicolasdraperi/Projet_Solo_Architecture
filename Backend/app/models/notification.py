from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String(255), nullable=False)
    dateEnvoi = Column(DateTime, nullable=False)
    joueur_id = Column(Integer, ForeignKey("joueurs.id"), nullable=False)

    joueur = relationship("Joueur", back_populates="notifications")
