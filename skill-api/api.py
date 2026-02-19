from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from groq import Groq
import json

app = FastAPI(title="Simulateur de Quiz")


client = Groq(api_key="cle api groq")

class QuizRequest(BaseModel):
    matiere: str
    theme: str
    niveau: str
    question_precedente: str | None = None
    reponse_etudiant: str | None = None

@app.post("/quiz")
def quiz(data: QuizRequest):

    if not data.question_precedente:
        prompt = f"""
        Tu es un professeur qui crée des quiz.
        Genere UNE question en JSON pour :
        Matiere : {data.matiere}
        Theme : {data.theme}
        Niveau : {data.niveau}

        Reponds strictement en JSON avec :
        {{
            "question": "texte de la question",
            "difficulte": "facile / moyen / difficile"
        }}
        """

    else:
        prompt = f"""
        Tu es un professeur qui corrige les réponses.

        Matiere : {data.matiere}
        Thème : {data.theme}
        Niveau : {data.niveau}

        Question précédente : {data.question_precedente}
        Reponse de l'etudiant : {data.reponse_etudiant}

        Corrige la reponse.
        Explique brievement.
        Puis genere une nouvelle question du même thème et niveau.

        Reponds strictemnt en JSON avec :
        {{
            "est_correct": true / false,
            "correction": "texte",
            "explication": "texte",
            "prochaine_question": "texte",
            "difficulte": "facile / moyen / difficile"
        }}
        """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )

        return json.loads(response.choices[0].message.content)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
