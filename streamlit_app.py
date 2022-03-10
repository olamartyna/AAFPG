import streamlit as st
import data_vis, playlist_visualisation, playlist  # home
st.set_page_config(layout="wide")

PAGES = {
    # "Home page": home,
    "Visualisation": playlist_visualisation,
    "Tensorflow Projector": data_vis,
    "Playlist": playlist
 }

st.sidebar.write('## Audio Analysis for Better Playlists')

selection = st.sidebar.radio('Menu', list(PAGES.keys()))
page = PAGES[selection]
page.app()
