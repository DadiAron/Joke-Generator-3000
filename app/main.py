from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from app.model_loader import generate_joke

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("static/index.html") as f:
        return HTMLResponse(f.read())

@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    joke = generate_joke(prompt)
    return JSONResponse(content={"joke": joke})