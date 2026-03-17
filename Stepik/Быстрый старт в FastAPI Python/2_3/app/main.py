from fastapi import FastAPI
from .models.Feedback import Feedback

app = FastAPI()

users = []

@app.post("/feedback")
async def post(feedback: Feedback):
    users.append({"name": feedback.name, "message": feedback.message})
    return {"message": f"Feedback received. Thank you, {feedback.name}."}

@app.get("/users_feed")
async def show_feedback():
    return users