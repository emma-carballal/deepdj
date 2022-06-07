from importlib import reload
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from deepdj.processing import deepdj_processing
import math

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

#@app.get("/")  # type: ignore
#def index():
#    return {"greeting": "Welcome to DeepDJ!"}

@app.get("/")
def playlist(text_input):
    dj1 = deepdj_processing('tcc_ceds_music_cleaned.csv')
    res = dj1.prompt_process(text_input)
    return {"res": res}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
    #uvicorn simple:fast --reload  # type: ignore
