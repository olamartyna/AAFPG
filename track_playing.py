import streamlit as st
import streamlit.components.v1 as components


# https://docs.streamlit.io/library/api-reference/media/st.audio

# search bar and audio playing

def track_playing():
    path = "/AAFPG/data/000002.mp3"
    title = st.text_input('Choose track title', '')
    st.write('The current movie title is', title)
    st.audio(path, format="audio/wav", start_time=0)


def app():
    track_playing()
