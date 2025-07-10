from fastapi import FastAPI
from app.routers import joueur_router 
from app.routers import coach_router
from app.core.database import Base, engine
import app.models.joueur
import app.models.coach
import app.models.session
import app.models.paiement
import app.models.notification

print("Création des tables...")
Base.metadata.create_all(bind=engine)
print("Terminé")

app = FastAPI(title="API Coaching")

# Inclure tes routers
app.include_router(joueur_router.router, prefix="/joueur", tags=["Joueur"])
app.include_router(coach_router.router, prefix="/coach", tags=["Coach"])

# Tu peux aussi faire pour les autres 
# app.include_router(admin_router.router, prefix="/admin", tags=["Admin"])
