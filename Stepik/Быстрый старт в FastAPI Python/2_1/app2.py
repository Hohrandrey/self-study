from fastapi import FastAPI
from fastapi.responses import FileResponse

app2 = FastAPI()

# альтернативный вариант
@app2.get("/file", response_class=FileResponse)
async def root_html():
    return "app2.html"

# версия для авто-установки файла
@app2.get("/download")
async def root_download():
    return FileResponse("app2.html",
            filename = "Читы.html",
            media_type = "application/octet-stream")

# первый вариант 
@app2.get("/")
async def root():
    return FileResponse("app2.html")
