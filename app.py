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

deepdj_api_url = "https://deepdj-7ah34aow4a-ew.a.run.app"
#deepdj_api_url = "http://127.0.0.1:8000"
params = {"text_input" : text_input}
response = requests.get(deepdj_api_url, params=params).json()
if response['res']!=0:
    st.write(pd.DataFrame.from_dict(response['res'], orient = 'index')) #turn JSON into DataFrame
   
    #pd.DataFrame.from_dict(response['res'], orient = 'index') #turn JSON into DataFrame
    #df = pd.read_csv("tcc_ceds_music_cleaned.csv", index_col=False)

    #indexes = response['res'].index


    #st.write('''
    #You will enjoy songs like:
    #''')
    #for idx in indexes:
    #df[["artist_name", "track_name"]].iloc[idx]
