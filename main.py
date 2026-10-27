import os
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
from typing import Optional  # ➕ AJOUT : Pour rendre le pseudo optionnel

# Imports pour MySQL
from sqlalchemy.orm import Session
import models
from database import get_db

# Charge les variables du fichier .env
load_dotenv()

app = FastAPI()

# Autorise le frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("GROQ_API_KEY non trouvée. Crée un fichier .env avec ta clé.")

client = Groq(api_key=api_key)

# 🔄 MODIFICATION : 'username' devient Optionnel. Plus d'erreur 422 !
class Question(BaseModel):
    username: Optional[str] = "Inconnu"
    message: str

@app.post("/chat")
def chat(question: Question, db: Session = Depends(get_db)):
    if not question.message or question.message.strip() == "":
        return {"response": "Veuillez saisir une question ou un message valide."}

    try:
        # --- VOTRE CODE D'ORIGINE POUR GROQ (STABLE ET INCHANGÉ) ---
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": question.message}]
        )
        reponse_ia = response.choices[0].message.content
        # -----------------------------------------------------------

        # ➕ AJOUT SÉCURISÉ : Sauvegarde dans MySQL uniquement si l'étudiant existe
        if question.username and question.username != "Inconnu":
            user = db.query(models.User).filter(models.User.username == question.username).first()
            if user:
                msg_utilisateur = models.ChatMessage(user_id=user.id, role="user", content=question.message)
                msg_ia = models.ChatMessage(user_id=user.id, role="assistant", content=reponse_ia)
                db.add(msg_utilisateur)
                db.add(msg_ia)
                db.commit()

        return {"response": reponse_ia}

    except Exception as e:
        if 'db' in locals():
            db.rollback()
        raise HTTPException(status_code=500, detail=f"Erreur : {str(e)}")
    

    # ➕ AJOUTER TOUT EN BAS DE MAIN.PY

@app.get("/history/{username}")
def get_chat_history(username: str, db: Session = Depends(get_db)):
    # 1. Chercher l'utilisateur dans MySQL
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé.")

    # 2. Récupérer tous ses messages stockés dans la base de données
    messages = db.query(models.ChatMessage)\
        .filter(models.ChatMessage.user_id == user.id)\
        .order_by(models.ChatMessage.id.asc())\
        .all()

    # 3. Renvoyer la liste des messages au format JSON
    historique = []
    for msg in messages:
        historique.append({
            "role": msg.role,
            "content": msg.content
        })

    return {"history": historique}


# ➕ CORRECTION : sans cette ligne, les routes /register et /login
# définies dans auth.py n'étaient JAMAIS ajoutées à l'application.
# Elle doit rester ICI, en bas du fichier, après la création de "app".
import auth  # noqa: E402,F401