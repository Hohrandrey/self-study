from fastapi import FastAPI
from .models.models import Feedback

app = FastAPI()

feedbacks = []

@app.post("/feedback")
async def post(feedback: Feedback):
    feedbacks.append({"name": feedback.name, "message": feedback.message})
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}

@app.get("/users_feeds")
async def show_feedback():
    return feedbacks