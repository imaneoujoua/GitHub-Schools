from sqlalchemy import Column, Integer, String, Date, Text, DateTime
import datetime
# On importe la classe Base que l'on a créée dans database.py
from database import Base

class User(Base):
    __tablename__ = "users"

    # Définition de chaque colonne pour correspondre exactement à votre table MySQL
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(100), unique=True, index=True, nullable=False)
    civilite = Column(String(20), nullable=False)
    nom = Column(String(100), nullable=False)
    prenom = Column(String(100), nullable=False)
    date_naissance = Column(Date, nullable=False)
    nationalite = Column(String(100), nullable=False)
    adresse = Column(Text, nullable=False)
    code_postal = Column(String(20), nullable=False)
    ville = Column(String(100), nullable=False)
    pays = Column(String(100), nullable=False)
    telephone = Column(String(30), nullable=False)
    email = Column(String(150), unique=True, index=True, nullable=False)
    niveau_profil = Column(String(100), nullable=False)
    hashed_password = Column(String(255), nullable=False) # Le mot de passe sera haché pour la sécurité
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, nullable=False) # Liaison avec l'ID de l'utilisateur
    role = Column(String(20), nullable=False)   # 'user' ou 'assistant'
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)