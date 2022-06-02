from importlib import reload
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from deepdj.processing import deepdj_processing

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
def playlist(text_input):
    dj1 = deepdj_processing('../deepdj/data/tcc_ceds_music_cleaned.csv')
    #return {"greeting": "Playlist"}
    return deepdj_processing.prompt_process()



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
    #uvicorn simple:fast --reload  # type: ignore
