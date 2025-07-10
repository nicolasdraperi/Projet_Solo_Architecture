from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services import joueur_service
from app.schemas import joueur as schemas_joueur
from app.schemas import session as schemas_session
from app.schemas import paiement as schemas_paiement
from app.schemas import notification as schemas_notification
from app.models import coach as models_coach
from app.models import session as models_session
from app.schemas import coach as schemas_coach

from app.dependencies import auth
from app.dependencies.auth import get_current_joueur

router = APIRouter(
    tags=["Joueur"]
)

#auth
@router.post("/login", response_model=schemas_joueur.JoueurToken)
def login(joueur: schemas_joueur.JoueurLogin, db: Session = Depends(get_db)):
    user = joueur_service.authenticate_joueur(db, joueur.email, joueur.password)
    if not user:
        raise HTTPException(status_code=400, detail="Email ou mot de passe incorrect")
    access_token = auth.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/inscription", response_model=schemas_joueur.JoueurOut)
def inscription(joueur: schemas_joueur.JoueurCreate, db: Session = Depends(get_db)):
    return joueur_service.create_joueur(db, joueur)

@router.get("/profile", response_model=schemas_joueur.JoueurOut)
def read_profile(current_user: schemas_joueur.JoueurOut = Depends(get_current_joueur)):
    return current_user


# routes publiques

@router.get("/coachs", response_model=list[schemas_coach.CoachOut])
def get_coachs(db: Session = Depends(get_db)):
    return joueur_service.get_all_coachs(db)

@router.get("/coach/{coach_id}/creneaux", response_model=list[schemas_session.SessionOut])
def get_creneaux(coach_id: int, db: Session = Depends(get_db)):
    return joueur_service.get_creneaux_by_coach(db, coach_id)


# routes privée
@router.post("/session/{session_id}/reserver", response_model=schemas_session.SessionOut)
def reserver_session(
    session_id: int,
    db: Session = Depends(get_db),
    current_user: schemas_joueur.JoueurOut = Depends(get_current_joueur)
):
    try:
        return joueur_service.reserver_session(db, current_user.id, session_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/session/{session_id}/payer", response_model=schemas_paiement.PaiementOut)
def payer_session(
    session_id: int,
    paiement: schemas_paiement.PaiementCreate,
    db: Session = Depends(get_db),
    current_user: schemas_joueur.JoueurOut = Depends(get_current_joueur)
):
    if session_id != paiement.session_id:
        raise HTTPException(status_code=400, detail="ID session non cohérent")
    return joueur_service.payer_session(db, session_id, paiement.montant)


@router.post("/notification", response_model=schemas_notification.NotificationOut)
def envoyer_notification(
    message: str,
    db: Session = Depends(get_db),
    current_user: schemas_joueur.JoueurOut = Depends(get_current_joueur)
):
    return joueur_service.envoyer_notification(db, current_user.id, message)
