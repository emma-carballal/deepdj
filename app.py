import streamlit as st
import requests
import pandas as pd

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
markdown = st.container()
with header:

    #st.title("Welcome to the DeepDJ!")
    st.markdown(f'<h1 style="color:#48c9f8;font-size:60px;text-align:center;">{"Welcome to DeepDj!"}</h1>', unsafe_allow_html=True)
    #st.success(st.markdown(f'<h1 style="color:#48c9f8;font-size:60px;text-align:center;">{"Welcome to DeepDj!”"}</h1>', unsafe_allow_html=True))
with dataset:
    #st.header("Music dataset 1950 to 2019 - Kaggle")
    st.markdown(f'<h1 style="color:#48c9f8;font-size:50px;text-align:center;">{"Music dataset 1950 to 2019 - Kaggle"}</h1>', unsafe_allow_html=True)

with features:
    #st.header("Project created by Emma Caballal, Julia Strahl, Gabriela Pimenta, Hatice Peucker")
    st.markdown(f'<h1 style="color:#48c9f8;font-size:30px;text-align:center;">{"Project created by Emma Caballal, Julia Strahl, Gabriela Pimenta, Hatice Peucker"}</h1>', unsafe_allow_html=True)


col4, col5, col6 = st.columns(3)

with col4:
    st.write(' ')
with col5:
    st.image("deepdjphotos/lyricoastergif.gif")
with col6:
    st.write(' ')

# Using the "with" syntax
with st.form(key='description_form'):
    st.markdown(f'<h1 style="color:#48c9f8;font-size:10 px;text-align:center;">{"Describe what you would like to hear!"}</h1>', unsafe_allow_html=True)
    text_input = st.text_input(label='')  # type: ignore
    submit_button = st.form_submit_button(label='Submit')


st.markdown(f'<h1 style="color:#48c9f8;font-size:6 px;text-align:center;">{"This is your perfect playlist:"}</h1>', unsafe_allow_html=True)





deepdj_api_url = "https://deepdj-7ah34aow4a-ew.a.run.app"
#deepdj_api_url = "http://127.0.0.1:8000"


params = {"text_input" : text_input}
response = requests.get(deepdj_api_url, params=params)
#if response.status_code == 200:
    #print("Empty response, try again")
if response.ok:
    response = response.json()

    if response['res']!=0:
#if response !=0:
        final_result = (pd.DataFrame.from_dict(response['res'], orient = 'index'))#turn JSON into DataFrame

        df = pd.read_csv("tcc_ceds_music_cleaned.csv", index_col=False)

        indexes = final_result.index

        st.markdown('''
        You will enjoy songs like:
        ''')
        for idx in indexes:
            list_lyrics=df[["artist_name", "track_name"]].iloc[int(idx)]
            st.write(list_lyrics)

else:
    st.write('I didn´t find anything. Please try again :)')
