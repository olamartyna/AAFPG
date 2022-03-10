import streamlit as st
import home, data_vis, playlist_visualisation
st.set_page_config(layout="wide")

PAGES = {
    "Home page": home,
    "Visualisation": playlist_visualisation,
    "Tensorflow Projector": data_vis
    "Playlist": playlist
 }

st.sidebar.write('### Menu')

selection = st.sidebar.radio('', list(PAGES.keys()))
page = PAGES[selection]
page.app()
