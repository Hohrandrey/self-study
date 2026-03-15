from fastapi import FastAPI


app = FastAPI()


@app.post("/feedback")
async def feedback():