import streamlit as st

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

'''
## Get a playlist

'''

# Using the "with" syntax
with st.form(key='my_form1'):
	text_input = st.text_input(label='Describe what you would  like to hear')
	submit_button = st.form_submit_button(label='Submit')

df = pd.read_csv("/Users/nineve/code/emma-carballal/deepdj/raw_data/tcc_ceds_music_cleaned.csv", index_col=False)
vectorizer = TfidfVectorizer(max_df = 0.75, max_features = 5000, ngram_range=(1,2))
vectorized_songs = pd.DataFrame(vectorizer.fit_transform(df["lyrics"]).toarray(),
                                 columns = vectorizer.get_feature_names_out())

vectorized_prompt = pd.DataFrame(vectorizer.transform([text_input]).toarray())
from scipy.spatial import distance

df["distance"] = [distance.cosine(vectorized_songs.iloc[k], vectorized_prompt) for k in range(len(vectorized_songs))]
closest = df["distance"].nsmallest(10)
indexes = closest.index

st.markdown('''
You will enjoy songs like like:
''')
for idx in indexes:
    df[["artist_name", "track_name"]].iloc[idx]
