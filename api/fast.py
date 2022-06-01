from importlib import reload
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")  # type: ignore
def index():
    return {"greeting": "Welcome to DeepDJ!"}

@app.get("/playlist")
def playlist():
    return {"greeting": "Playlist"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
    #uvicorn simple:fast --reload  # type: ignore
