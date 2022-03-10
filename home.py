# home page

import streamlit as st

def welcome():
    st.title('AUDIO ANALYSIS FOR BETTER PLAYLIST')


    st.image('librosa-feature-melspectrogram-1.png')
    # file source: https://librosa.org/doc/main/generated/librosa.feature.melspectrogram.html

def app():
    welcome()
