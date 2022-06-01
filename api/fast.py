from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers

@app.get("/")  # type: ignore
def index():
    return {"greeting": "Welcome to DeepDJ!"}

@app.get("/playlist")
def playlist():
    return {"greeting": "Playlist"}