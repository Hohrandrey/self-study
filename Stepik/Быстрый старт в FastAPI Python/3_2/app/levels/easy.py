"""
#Лёгкий уровень

db = {
  "username": "user123",
  "password": "password123"
}

@app.get("/user")
async def user(session_token=Cookie(None)):
    if session_token in sessions:
        return {
            "username": db["username"],
            "message": "Authorized successfully"
        }
    return {"message": "Unauthorized"}
"""