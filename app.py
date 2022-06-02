import streamlit as st

header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
modelTraining = st.beta_container()

with header:
    st.title("Welcome to the DeepDJ!")

with dataset:
    st.header("Music Dataset 1950 to 2019 - Kaggle")
with features:
    st.header("Features are created by Emma Caballal, Julia Strahl, Gabriela Pimenta, Hatice Peucker")

with features:
    features("Let's train together!:)")


'''
## Get a playlist

'''

# Using the "with" syntax
with st.form(key='my_form1'):
	text_input = st.text_input(label='Describe what you would  like to hear')
	submit_button = st.form_submit_button(label='Submit')

st.markdown('''
You want to listen to something like:
''')
text_input
