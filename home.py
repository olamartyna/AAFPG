# home page

import streamlit as st

def welcome():
    # st.title('AUDIO ANALYSIS FOR BETTER PLAYLIST')

    # from PIL import Image
    # image = Image.open('AAFPG/data/home page image.jpg')
    # st.image(image)
    path_github = "/app/aafpg/"
    st.image(path_github + 'AAFPG/data/home page image.jpg', width = 1400)


def app():
    welcome()
