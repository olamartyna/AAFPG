# home page

import streamlit as st

def welcome():
    st.title('Autoencoding Audio Features For Playlist Generation')
    st.write('This is our embedding')  # imporve font

    st.image('librosa-feature-melspectrogram-1.png')
    # file source: https://librosa.org/doc/main/generated/librosa.feature.melspectrogram.html

def app():
    welcome()
