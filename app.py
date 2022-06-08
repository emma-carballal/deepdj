import streamlit as st
import requests
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

DATE_COLUMN = 'date/time'
DATA_URL = ('tcc_ceds_music_cleaned.csv')
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    st.image("deepdjphotos/deedjmanlogogif.gif")
with col3:
    st.write(' ')
header = st.container()
dataset = st.container()
features = st.container()
with header:
    st.title("Welcome to the DeepDJ!")
with dataset:
    st.header("Music Dataset 1950 to 2019 - Kaggle")
with features:
    st.header("Features are created by Emma Caballal, Julia Strahl, Gabriela Pimenta, Hatice Peucker")
    st.header("Let's train our model together")

col4, col5, col6 = st.columns(3)

with col4:
    st.write(' ')
with col5:
    st.image("deepdjphotos/lyricoastergif.gif")
with col6:
    st.write(' ')

# Using the "with" syntax
with st.form(key='description_form'):
    text_input = st.text_input(label='Describe what you would like to hear in your playlist!')
    submit_button = st.form_submit_button(label='Submit')
st.markdown('''
You want to listen to something like:
''')
text_input

with st.form(key='columns_in_form'):
    cols = st.columns(5)
    for i, col in enumerate(cols):
        col.selectbox(f'Make a Selection', ['click', 'or click'], key=i)
    submitted = st.form_submit_button('Submit')

deepdj_api_url = "https://deepdj-7ah34aow4a-ew.a.run.app"
#deepdj_api_url = "http://127.0.0.1:8000"

params = {"text_input" : text_input}
response = requests.get(deepdj_api_url, params=params).json()
if response['res']!=0:
    final_result = (pd.DataFrame.from_dict(response['res'], orient = 'index'))#turn JSON into DataFrame

    df = pd.read_csv("tcc_ceds_music_cleaned.csv", index_col=False)

    indexes = final_result.index


    st.markdown('''
    You will enjoy songs like:
    ''')
    for idx in indexes:
        list_lyrics=df[["artist_name", "track_name"]].iloc[int(idx)]
        st.write(list_lyrics)
