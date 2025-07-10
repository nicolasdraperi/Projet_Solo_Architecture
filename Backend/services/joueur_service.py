from sqlalchemy.orm import Session
from app.models import joueur as models_joueur
from app.models import coach as models_coach
from app.models import session as models_session
from app.models import paiement as models_paiement
from app.models import notification as models_notification

from app.schemas import joueur as schemas_joueur
from app.schemas import session as schemas_session
from app.schemas import paiement as schemas_paiement
from app.schemas import notification as schemas_notification

from app.dependencies import auth
import bcrypt
from datetime import datetime, timezone

def authenticate_joueur(db, email, password):
    joueur = db.query(models_joueur.Joueur).filter(models_joueur.Joueur.email == email).first()
    if not joueur or not auth.verify_password(password, joueur.password):
        return None
    return joueur


def create_joueur(db: Session, joueur: schemas_joueur.JoueurCreate):
    hashed_password = bcrypt.hashpw(joueur.password.encode('utf-8'), bcrypt.gensalt())
    db_joueur = models_joueur.Joueur(
        nom=joueur.nom,
        email=joueur.email,
        password=hashed_password.decode('utf-8')
    )
    db.add(db_joueur)
    db.commit()
    db.refresh(db_joueur)
    return db_joueur

def get_all_coachs(db: Session):
    return db.query(models_coach.Coach).all()

def get_creneaux_by_coach(db: Session, coach_id: int):
    return db.query(models_session.Session).filter(
        models_session.Session.coach_id == coach_id,
        models_session.Session.statut == "disponible"
    ).all()

def reserver_session(db: Session, joueur_id: int, session_id: int):
    session_obj = db.query(models_session.Session).filter(
        models_session.Session.id == session_id
    ).first()

    if session_obj is None or session_obj.statut != "disponible":
        raise Exception("Session non disponible.")

    session_obj.joueur_id = joueur_id
    session_obj.statut = "réservée"
    db.commit()
    db.refresh(session_obj)
    return session_obj

def payer_session(db: Session, session_id: int, montant: float):
    paiement = models_paiement.Paiement(
        session_id=session_id,
        montant=montant,
        date=datetime.now(timezone.utc)
,
        statut="payé"
    )
    db.add(paiement)
    db.commit()
    db.refresh(paiement)
    return paiement


def envoyer_notification(db: Session, joueur_id: int, message: str):
    notif = models_notification.Notification(
        joueur_id=joueur_id,
        message=message,
        dateEnvoi=datetime.utcnow()
    )
    db.add(notif)
    db.commit()
    db.refresh(notif)
    return notif

def get_reservations_for_joueur(db: Session, joueur_id: int):
    return db.query(models_session.Session).filter(models_session.Session.joueur_id == joueur_id).all()
