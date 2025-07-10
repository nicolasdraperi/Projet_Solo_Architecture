from core.database import Base, engine
import models.joueur
import models.coach
import models.session
import models.paiement
import models.notification

print("Création des tables...")
Base.metadata.create_all(bind=engine)
print("Terminé")
