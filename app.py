import streamlit as st
import requests

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

'''
## Get a playlist

'''

# Using the "with" syntax
with st.form(key='my_form1'):
	text_input = st.text_input(label='Describe what you would  like to hear')
	submit_button = st.form_submit_button(label='Submit')



#deepdj_api_url = f"http://127.0.0.1:8000/playlist?{text_input}"

#response = requests.get(
    #deepdj_api_url
#).json()

#print(response)

deepdj_api_url = "http://127.0.0.1:8000/"
params = {"text_input" : text_input}
response = requests.get(deepdj_api_url, params=params).json()
print(response)

# df = pd.read_csv("deepdj/data/tcc_ceds_music_cleaned.csv", index_col=False)
# vectorizer = TfidfVectorizer(max_df = 0.75, max_features = 5000, ngram_range=(1,2))
# vectorized_songs = pd.DataFrame(vectorizer.fit_transform(df["lyrics"]).toarray(),
#                                  columns = vectorizer.get_feature_names_out())

# vectorized_prompt = pd.DataFrame(vectorizer.transform([text_input]).toarray())
# from scipy.spatial import distance

# df["distance"] = [distance.cosine(vectorized_songs.iloc[k], vectorized_prompt) for k in range(len(vectorized_songs))]
# closest = df["distance"].nsmallest(10)
# indexes = closest.index

# st.markdown('''
# You will enjoy songs like like:
# ''')
# for idx in indexes:
#     df[["artist_name", "track_name"]].iloc[idx]
