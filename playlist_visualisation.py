import streamlit as st
import streamlit.components.v1 as components
from data_vis import path_github
import pandas as pd
import plotly.express as px

import pandas as pd
import numpy as np
import os
import IPython
from IPython.display import Audio
import random
import warnings
from scipy.spatial import distance

from functions import play_track, cohesive_playlist, progressive_playlist

# https://docs.streamlit.io/library/api-reference/media/st.audio


path_github = ""
tracks_path = path_github + 'AAFPG/data/tracks_info.csv'
tracks = pd.read_csv(tracks_path, index_col = 0)
tracks['combined_info'] = tracks['artist_name']+' - '+tracks['track_title']+' - '+tracks['genre']

ml_pca_path = path_github + 'AAFPG/data/ml_pca.csv'
ml_pca = pd.read_csv(ml_pca_path, index_col = 0)


def choose_playlist_length():
    playlist_length = st.selectbox(
        'Playlist lenght?', (range(5, 21))
    )

def choose_track():

    no_song= pd.Series(["No song selected"])
    option = st.selectbox(
        'What are we playing?',
        (no_song.append(tracks['combined_info']))  #pass on a column from df to have list of artists
    )
    st.write('You selected:', option)
    track_id = tracks.index[tracks['combined_info']==option][0]
    st.write('Track ID = ', track_id)
    # st.audio(path_github +"/AAFPG/data/000002.mp3", format="audio/wav", start_time=0)
    return track_id

def plot_ml_pca(track_id, show_all = False):

    if show_all:
        ml_pca_working = ml_pca
    else:
        ml_pca_working = ml_pca.loc[[track_id]]

    x, y, z = ml_pca_working['PC1'], ml_pca_working['PC2'], ml_pca_working['PC3']
    x_range = [ml_pca['PC1'].min(), ml_pca['PC1'].max()]
    y_range = [ml_pca['PC2'].min(), ml_pca['PC2'].max()]
    z_range = [ml_pca['PC3'].min(), ml_pca['PC3'].max()]
    range_x = x_range
    color = tracks['genre'].loc[ml_pca_working.index]
    fig = px.scatter_3d(x = x, y = y, z = z, color = color, range_x = y_range, range_y = y_range, range_z = z_range)
    fig.update_layout(title='Machine Learning PCA', autosize=False, width=800, height=800, margin=dict(l=40, r=40, b=40, t=40))
    st.plotly_chart(fig)




def show_all():
    show_all = st.selectbox('Show all tracks?', ('Yes', 'No'))
    if show_all == 'Yes':
        return True
    else:
        return False




def app():
    #choose_track()
    track_id = choose_track()
    # show_all()
    show_all_1 = show_all()
    plot_ml_pca(track_id, show_all_1)
    choose_playlist_length()
