import streamlit as st
import pandas as pd 
import sys
sys.path.append("..")
from fakenews.inference import make_predictions

st.title('Fake News Detection')

with st.form("my_form"):
    title = st.text_input(label='Enter Title', type="default", help=None, autocomplete=None, on_change=None, placeholder='Title')
    author =  st.text_input(label='Enter Author Name', on_change=None, placeholder='Author Name')
    description = st.text_area(label='Enter the description', placeholder='Description')
    data = pd.DataFrame(data=[[title,author,description]],columns=['title','author','text'])
    y_pred = make_predictions(data)
    submitted = st.form_submit_button("Submit")
    if submitted is True and title != '' and author != '' and description != '':
        if y_pred == 1:
            st.write("This is Fake News")
        else:
            st.write("This is Correct News")
    elif submitted is True and title == '' and author == '' and description == '':
        st.error('Enter all the input values')