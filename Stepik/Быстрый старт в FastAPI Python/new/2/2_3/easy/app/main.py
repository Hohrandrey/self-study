from fastapi import FastAPI
from .models.feedback import Feedback

app = FastAPI()
feedbacks_list = []


@app.post('/feedback')
async def get_feedback(feedback: Feedback):
    feedbacks_list.append(feedback)
    return {"message": f"Feedback received. Thank you, {feedback.name}."}

@app.get('/feedbacks')
async def get_feedbacks():
    return {"feedbacks": feedbacks_list}