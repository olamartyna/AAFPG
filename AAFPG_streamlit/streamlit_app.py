import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st



import home, dataframe, track_playing, playlist, data_vis


PAGES = {
    "Home page": home,
    "Dataframe": dataframe,
    "Data Visualisation": data_vis,
    "Track playing": track_playing,
    "Playlist": playlist
}

st.sidebar.write('### Navigation')

selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
