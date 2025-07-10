import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Charge les variables d'environnement
env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(env_path)

# Récupère l'URL de connexion
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in .env file!")

# Crée l'engine
engine = create_engine(
    DATABASE_URL,
    echo=True,  # mets False en prod
    pool_pre_ping=True
)

# Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base pour tes models
Base = declarative_base()
