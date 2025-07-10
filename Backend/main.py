from fastapi import FastAPI

from routers import joueur_router
from routers import coach_router
from core.database import Base, engine
import models.joueur
import models.coach
import models.session
import models.paiement
import models.notification

from fastapi.middleware.cors import CORSMiddleware


print("Création des tables...")
Base.metadata.create_all(bind=engine)
print("Terminé")

app = FastAPI(title="API Coaching")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # autorise ton front
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclure tes routers
app.include_router(joueur_router.router, prefix="/joueur", tags=["Joueur"])
app.include_router(coach_router.router, prefix="/coach", tags=["Coach"])

# Tu peux aussi faire pour les autres 
# app.include_router(admin_router.router, prefix="/admin", tags=["Admin"])
