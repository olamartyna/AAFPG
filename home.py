# home page

import streamlit as st

def welcome():
    # st.title('AUDIO ANALYSIS FOR BETTER PLAYLIST')

    # from PIL import Image
    # image = Image.open('AAFPG/data/home page image.jpg')
    # st.image(image)

    path_github = "/app/aafpg/"

    st.image(path_github + 'AAFPG/data/home page image.jpg', width = 1100)

    # col1, col2, col3 = st.beta_columns([1,6,1])

    # with col1:
    # st.write("")

    # with col2:
    # st.image("path_github + 'AAFPG/data/home page image.jpg")

    # with col3:
    # st.write("")
def app():
    # with open('style.css') as f:
    #     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

    welcome()
