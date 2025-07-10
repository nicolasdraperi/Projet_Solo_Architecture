from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.database import get_db
from services import coach_service
from schemas import coach as schemas_coach
from schemas import session as schemas_session

from dependencies import auth
from dependencies.auth import get_current_coach

router = APIRouter(
    tags=["Coach"]
)


# authentification


@router.post("/login", response_model=schemas_coach.CoachToken)
def login(coach: schemas_coach.CoachLogin, db: Session = Depends(get_db)):
    user = coach_service.authenticate_coach(db, coach.email, coach.password)
    if not user:
        raise HTTPException(status_code=400, detail="Email ou mot de passe incorrect")
    access_token = auth.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

# CRUD des créneaux
@router.post("/creneaux", response_model=schemas_session.SessionOut)
def create_creneau(
    creneau: schemas_session.SessionCreate,
    db: Session = Depends(get_db),
    current_coach: schemas_coach.CoachOut = Depends(get_current_coach)
):
    return coach_service.create_creneau(db, current_coach.id, creneau)

@router.put("/creneaux/{creneau_id}", response_model=schemas_session.SessionOut)
def update_creneau(
    creneau_id: int,
    creneau_update: schemas_session.SessionUpdate,
    db: Session = Depends(get_db),
    current_coach: schemas_coach.CoachOut = Depends(get_current_coach)
):
    try:
        return coach_service.update_creneau(db, current_coach.id, creneau_id, creneau_update)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/creneaux/{creneau_id}")
def delete_creneau(
    creneau_id: int,
    db: Session = Depends(get_db),
    current_coach: schemas_coach.CoachOut = Depends(get_current_coach)
):
    try:
        return coach_service.delete_creneau(db, current_coach.id, creneau_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


#confirmer / refuser réservation


@router.put("/reservation/{session_id}/statut")
def changer_statut_reservation(
    session_id: int,
    nouveau_statut: str,
    db: Session = Depends(get_db),
    current_coach: schemas_coach.CoachOut = Depends(get_current_coach)
):
    try:
        return coach_service.changer_statut_reservation(db, current_coach.id, session_id, nouveau_statut)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

#consulter planning
@router.get("/planning", response_model=list[schemas_session.SessionOut])
def get_planning(
    db: Session = Depends(get_db),
    current_coach: schemas_coach.CoachOut = Depends(get_current_coach)
):
    return coach_service.get_planning(db, current_coach.id)


@router.post("/create", response_model=schemas_coach.CoachOut)
def create_coach(coach: schemas_coach.CoachCreate, db: Session = Depends(get_db)):
    return coach_service.create_coach(db, coach)

