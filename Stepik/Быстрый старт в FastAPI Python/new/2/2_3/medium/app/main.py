from fastapi import FastAPI
from .models.Feedback import Feedback


app = FastAPI()
feeds_list = []


@app.post('/feedback')
async def create_feedback(feedback: Feedback):
    print(feedback)
    feeds_list.append(feedback)
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}


@app.get('/feedbacks')
async def get_feedbacks():
    return feeds_list