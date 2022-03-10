# home page

import streamlit as st

def welcome():
    # st.title('AUDIO ANALYSIS FOR BETTER PLAYLIST')

    # from PIL import Image
    # image = Image.open('AAFPG/data/home page image.jpg')
    # st.image(image)

    path_github = "/app/aafpg/"
    # col1= st.columns(1)

    st.image(path_github + 'AAFPG/data/home page image.jpg', width = 1100)

def app():
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

    welcome()
