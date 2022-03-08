import streamlit as st
import streamlit.components.v1 as components


# https://docs.streamlit.io/library/api-reference/media/st.audio

# search bar and audio playing

def track_playing():
    track_id = '../AAFPG/data/000010.mp3'
    title = st.text_input('Choose track title', '')
    st.write('The current movie title is', title)
    st.audio(track_id, format="audio/wav", start_time=0)


def app():
    track_playing()
