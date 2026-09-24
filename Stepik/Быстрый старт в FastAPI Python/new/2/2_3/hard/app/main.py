from fastapi import FastAPI
from .models.Feedback import Feedback


app = FastAPI()
feeds_list = []


@app.post('/feedbacks')
async def get_feedbacks(feed: Feedback, is_premium: bool = False):
    prem_sub_str = ''
    if is_premium:
        prem_sub_str = ' Ваш отзыв будет рассмотрен в приоритетном порядке.'
    string = {'message': f"Спасибо, {feed.name}! Ваш отзыв сохранён.{prem_sub_str}"}
    feeds_list.append(string)
    return string

@app.get('/feedbacks')
async def get_feedbacks():
    return feeds_list