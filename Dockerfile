FROM python:3.8-buster
COPY api /api
COPY deepdj /deepdj
COPY tcc_ceds_music_cleaned.csv /tcc_ceds_music_cleaned.csv
COPY tfidf.pickle /tfidf.pickle
COPY vectorized_lyrics.pickle /vectorized_lyrics.pickle
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -m nltk.downloader all -d /usr/local/nltk_data
CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
