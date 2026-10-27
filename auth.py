import datetime
from fastapi import HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt

# Importation de vos configurations existantes
import models
from database import get_db
from main import app  # Garde le lien direct vers votre main stable

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 🔑 CONFIGURATION SÉCURITÉ JWT (À modifier avec vos propres valeurs secrètes)
SECRET_KEY = "VOTRE_CLE_SUPER_SECRETE_GITHUB_SCHOOLS_2026"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120  # Le jeton reste valide pendant 2 heures

# Fonctions utilitaires pour le Jeton
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# ----------------------------------------------------------------
# SCHÉMAS DE DONNÉES
# ----------------------------------------------------------------
class UserRegister(BaseModel):
    civilite: str
    username: str
    nom: str
    prenom: str
    date_naissance: str
    nationalite: str
    adresse: str
    code_postal: str
    ville: str
    pays: str
    telephone: str
    email: EmailStr
    niveau_profil: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

# ----------------------------------------------------------------
# ROUTES MISES À JOUR
# ----------------------------------------------------------------

@app.post("/register")
def register(user_data: UserRegister, db: Session = Depends(get_db)):
    user_exists = db.query(models.User).filter(
        (models.User.username == user_data.username) | (models.User.email == user_data.email)
    ).first()
    
    if user_exists:
        raise HTTPException(status_code=400, detail="Ce pseudonyme ou cet e-mail est déjà utilisé.")

    try:
        date_obj = datetime.datetime.strptime(user_data.date_naissance, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Format de date de naissance invalide (AAAA-MM-JJ).")

    hashed_pwd = pwd_context.hash(user_data.password)

    new_user = models.User(
        username=user_data.username,
        civilite=user_data.civilite,
        nom=user_data.nom,
        prenom=user_data.prenom,
        date_naissance=date_obj,
        nationalite=user_data.nationalite,
        adresse=user_data.adresse,
        code_postal=user_data.code_postal,
        ville=user_data.ville,
        pays=user_data.pays,
        telephone=user_data.telephone,
        email=user_data.email,
        niveau_profil=user_data.niveau_profil,
        hashed_password=hashed_pwd
    )
    
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erreur MySQL : {str(e)}")
    
    # On génère un token dès l'inscription pour connecter l'utilisateur immédiatement
    token = create_access_token(data={"sub": new_user.username, "user_id": new_user.id})
    return {
        "status": "success", 
        "token": token, 
        "prenom": new_user.prenom
    }

@app.post("/login")
def login(credentials: UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == credentials.username).first()
    
    if not user or not pwd_context.verify(credentials.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Identifiants ou mot de passe incorrects.")

    # Génération du Jeton sécurisé contenant le pseudo et l'ID unique
    token = create_access_token(data={"sub": user.username, "user_id": user.id})
    
    return {
        "status": "success", 
        "token": token, 
        "prenom": user.prenom
    }