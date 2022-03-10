import streamlit as st
import home, data_vis, playlist_visualisation


PAGES = {
    "Home page": home,
    "Visualisation": playlist_visualisation,
    "Tensorflow Projector": data_vis
 }

st.sidebar.write('### Menu')

selection = st.sidebar.radio('', list(PAGES.keys()))
page = PAGES[selection]
page.app()
