import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Charger les variables d'environnement (.env)
load_dotenv()

# Configuration des identifiants de votre MySQL local
# Par défaut avec XAMPP/Wamp : utilisateur = 'root' et pas de mot de passe ''
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")  # Mettez votre mot de passe si vous en avez un
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "github_schools")

# URL de connexion au format SQLAlchemy pour MySQL
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Création du moteur de liaison avec MySQL
engine = create_engine(DATABASE_URL)

# Usine à connexions (Sessions)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe de base pour concevoir nos futures tables en Python
Base = declarative_base()

# Fonction magique (Dependency) pour ouvrir la BDD au début d'une requête et la fermer à la fin
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()