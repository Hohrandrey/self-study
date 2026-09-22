from fastapi import FastAPI

app = FastAPI()
@app.get('/headers')
async def get_headers():
    pass

@app.get('/info')
async def get_info():
    pass