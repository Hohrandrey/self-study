from fastapi import FastAPI
from .models.models import Feedback

app = FastAPI()

feedbacks = []


@app.post("/feedback")
async def post(feedback: Feedback, is_premium: bool = False):
    feedbacks.append({"name": feedback.name, "message": feedback.message})
    answer = f"Спасибо, {feedback.name}! Ваш отзыв сохранён."
    if is_premium:
        answer += "Ваш отзыв будет рассмотрен в приоритетном порядке."
    return {"message": answer}


@app.get("/users_feeds")
async def show_feedback():
    return feedbacks
