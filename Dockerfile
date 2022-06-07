FROM python:3.8.6-buster
COPY api /api
COPY deepdj /deepdj
COPY tcc_ceds_music_cleaned.csv /tcc_ceds_music_cleaned.csv
COPY tfidf.pickle /tfidf.pickle
COPY vectorized_lyrics.pickle /vectorized_lyrics.pickle
#COPY /Users/Pimenta/code/GabiPimenta29/gcp/lunar-inn-346918-f23c3084971a.json /lunar-inn-346918-f23c3084971a.json
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
