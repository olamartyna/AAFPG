import streamlit as st
import playlist_visualisation, data_vis
st.set_page_config(layout="wide")

PAGES = {
    # "Home page": home,
    "Visualisation": playlist_visualisation,
    "Tensorflow Projector": data_vis
 }

st.sidebar.write('## Audio Analysis for Better Playlists')

selection = st.sidebar.radio('Menu', list(PAGES.keys()))
page = PAGES[selection]
page.app()
