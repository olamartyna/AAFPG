import streamlit as st
import streamlit.components.v1 as components

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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


path_github = "/app/aafpg/"
tracks_path = path_github + 'AAFPG/data/metadata_with_vectors_reduced.csv'
tracks = pd.read_csv(tracks_path, index_col = 0)
tracks['combined_info'] = tracks['artist_name']+' - '+tracks['track_title']+' - '+tracks['track_genre_top']

dl_tsne_path = path_github + 'AAFPG/data/dl_cnn_tsne.csv'
dl_tsne = pd.read_csv(dl_tsne_path, index_col = 0)


tracks = tracks.loc[list(dl_tsne.index)]

no_song= pd.Series(["No song selected"])
options= no_song.append(tracks['combined_info'])

def initialize_state():
    st.session_state.track1 = None
    st.session_state.track2 = None
    st.session_state.show_all = 'Yes'
    st.session_state.length = 10


def choose_playlist_length():
    lenght= st.selectbox(
        'Playlist lenght?', (range(5, 21)), key= 'length'
    )

def choose_track():

    track_id = tracks.index[tracks['combined_info']==st.session_state.choose_track1][0]

    # st.audio(path_github +"/AAFPG/data/000002.mp3", format="audio/wav", start_time=0)
    if st.session_state.choose_track1 == "No song selected":
        st.session_state.track1 = ""
    st.session_state.track1 = track_id

def choose_track2():

    track_id = tracks.index[tracks['combined_info']==st.session_state.choose_track2][0]

    # st.audio(path_github +"/AAFPG/data/000002.mp3", format="audio/wav", start_time=0)
    if st.session_state.choose_track2 == "No song selected":
        st.session_state.track2 = ""
    st.session_state.track2 = track_id

def plot_dl_tsne(track_id_1=None, track_id_2=None, show_all = 'Yes', playlist_len=10):

    if show_all=='Yes':
        playlist_display(dl_tsne, track=None)

    elif track_id_1 != None and track_id_2 != None:
        playlist= progressive_playlist(track_1=track_id_1, track_2=track_id_2,  df=dl_tsne, playlist_len=playlist_len, cosine=False)
        playlist_display(dl_tsne, track=playlist)

    else:
        playlist= cohesive_playlist(base_track=track_id_1, df=dl_tsne, playlist_len=playlist_len, cosine=False)
        playlist_display(dl_tsne, track=playlist)
        #playlist_display(dl_tsne, track=[track_id_1, track_id_2])



def playlist_display(df, track=None):
    ''''''
    op=1
    if track != None:
        op = 0.1
    df = dl_tsne.merge(tracks['track_genre_top'], left_index=True, right_index=True)
    fig = go.Figure(data=px.scatter_3d(df,
        x=df['0'].values,
        y=df['1'].values,
        z=df['2'].values,
        color= df['track_genre_top'],
        size= np.full(len(df['track_genre_top']), 0.2),
        #marker=dict(
        #    color= 'blue',
        #    size=3,
        #),
        #line=dict(
        #    color='white',
        #    width=0.1
        #),
        #showlegend=True,
        #legendgroup='track_genre_top',
        #hoverinfo='skip',
        opacity=op,
        #hovertext=list(df.index),
        #name= 'Full tracks database'
        ))
    if track != None:
        selected_tracks = df.loc[list(track)]
        fig.add_scatter3d(
            x=selected_tracks['0'].values,
            y=selected_tracks['1'].values,
            z=selected_tracks['2'].values,
            marker=dict(
                size=8,
            ),
            line=dict(
                color='darkblue',
                width=3
            ),
            hovertext=list(selected_tracks.index),
            name= 'Selected tracks'
        )

    fig.update_layout(title='Deep Learning TSNE', autosize=False, width=800, height=800, margin=dict(l=40, r=40, b=40, t=40))
    st.plotly_chart(fig)


def show_all():
    show_all = st.selectbox('Show all tracks?', ('Yes', 'No'), key='show_all')
    if show_all == 'Yes':
        return True
    else:
        return False




def app():
    #
    if 'track1' not in st.session_state:
        initialize_state()
    plot_dl_tsne(track_id_1=st.session_state.track1, track_id_2=st.session_state.track2, show_all=st.session_state.show_all, playlist_len=st.session_state.length)

    #choose_track()

    option1 = st.selectbox(
        'What are we playing?',
        options,  #pass on a column from df to have list of artists
        key='choose_track1',
        on_change = choose_track
    )
    st.write('You selected:', option1)
    st.write('Track ID = ', st.session_state.track1)


    option2 = st.selectbox(
        'Choose a second song if you want a progressive list',
        options,  #pass on a column from df to have list of artists
        key='choose_track2',
        on_change = choose_track2
    )
    st.write('You selected:', option2)
    st.write('Track ID = ', st.session_state.track2)


    # show_all()

    st.selectbox('Show all tracks?', ('Yes', 'No'), key='show_all')
    choose_playlist_length()
