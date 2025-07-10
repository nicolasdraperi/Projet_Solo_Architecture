from sqlalchemy.orm import Session
import models
from schemas import coach as schemas_coach
from schemas import session as schemas_session
from models import coach as models_coach
from models import session as models_session
from dependencies import auth
import bcrypt
from datetime import datetime


def authenticate_coach(db: Session, email: str, password: str):
    coach = db.query(models_coach.Coach).filter(models_coach.Coach.email == email).first()
    if not coach:
        return None
    if not bcrypt.checkpw(password.encode('utf-8'), coach.password.encode('utf-8')):
        return None
    return coach

def create_creneau(db: Session, coach_id: int, creneau: schemas_session.SessionCreate):
    new_creneau = models_session.Session(
        coach_id=coach_id,
        date_heure=creneau.date_heure,
        duree_minutes=creneau.duree_minutes,
        prix=creneau.prix,
        joueur_id=None,
        statut="disponible"
    )
    db.add(new_creneau)
    db.commit()
    db.refresh(new_creneau)
    return new_creneau

def update_creneau(db: Session, coach_id: int, creneau_id: int, creneau_update: schemas_session.SessionUpdate):
    creneau = db.query(models_session.Session).filter(models_session.Session.id == creneau_id, models_session.Session.coach_id == coach_id).first()
    if not creneau:
        raise Exception("Créneau non trouvé ou accès interdit")
    
    creneau.date_heure = creneau_update.date_heure
    creneau.duree_minutes = creneau_update.duree_minutes
    creneau.prix = creneau_update.prix
    db.commit()
    db.refresh(creneau)
    return creneau

def delete_creneau(db: Session, coach_id: int, creneau_id: int):
    creneau = db.query(models_session.Session).filter(models_session.Session.id == creneau_id, models_session.Session.coach_id == coach_id).first()
    if not creneau:
        raise Exception("Créneau non trouvé ou accès interdit")
    db.delete(creneau)
    db.commit()
    return {"detail": "Créneau supprimé"}

def changer_statut_reservation(db: Session, coach_id: int, session_id: int, nouveau_statut: str):
    if nouveau_statut not in ["confirmée", "refusée"]:
        raise Exception("Statut invalide")
    session = db.query(models_session.Session).filter(models_session.Session.id == session_id, models_session.Session.coach_id == coach_id).first()
    if not session:
        raise Exception("Session non trouvée ou accès interdit")
    if session.joueur_id is None:
        raise Exception("Cette session n'a pas encore de réservation")
    
    session.statut = nouveau_statut
    db.commit()
    db.refresh(session)
    return session

def get_planning(db: Session, coach_id: int):
    sessions = db.query(models_session.Session).filter(models_session.Session.coach_id == coach_id).all()
    return sessions


def create_coach(db: Session, coach: schemas_coach.CoachCreate):
    hashed_password = bcrypt.hashpw(coach.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    new_coach = models_coach.Coach(
        nom=coach.nom,
        email=coach.email,
        specialite=coach.specialite,
        password=hashed_password
    )
    db.add(new_coach)
    db.commit()
    db.refresh(new_coach)
    return new_coach


