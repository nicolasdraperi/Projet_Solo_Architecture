from app.core.database import Base, engine
import app.models.joueur
import app.models.coach
import app.models.session
import app.models.paiement
import app.models.notification

print("Création des tables...")
Base.metadata.create_all(bind=engine)
print("Terminé")
