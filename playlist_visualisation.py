import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

from functions import cohesive_playlist, progressive_playlist

st.set_page_config(layout="wide")

path_github = ""
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
    st.session_state.show_playlist = 'Yes'
    st.session_state.length = 10


def choose_playlist_length():
    lenght= st.selectbox(
        'Playlist lenght?', (range(5, 21)), key= 'length'
    )

def choose_track():

    if st.session_state.choose_track1 == "No song selected":
        st.session_state.track1 = None
    else:
        track_id = tracks.index[tracks['combined_info']==st.session_state.choose_track1][0]
        st.session_state.track1 = track_id

def choose_track2():

    if st.session_state.choose_track2 == "No song selected":
        st.session_state.track2 = None
    else:
        track_id = tracks.index[tracks['combined_info']==st.session_state.choose_track2][0]
        st.session_state.track2 = track_id



def plot_dl_tsne(track_id_1=None,
                 track_id_2=None,
                 show_playlist = 'No',
                 playlist_len=10):

    if show_playlist=='No':
        playlist_display(dl_tsne, track=None)
        playlist=[]

    elif track_id_1 != None and track_id_2 != None:
        playlist= progressive_playlist(track_1=track_id_1, track_2=track_id_2,  df=dl_tsne, playlist_len=playlist_len, cosine=False)
        playlist_display(dl_tsne, track=playlist)

    elif track_id_1 != None and track_id_2 == None:
        playlist= cohesive_playlist(base_track=track_id_1, df=dl_tsne, playlist_len=playlist_len, cosine=False)
        playlist_display(dl_tsne, track=playlist)
    else:
        playlist_display(dl_tsne, track=None)
        playlist=[]

    playlist_df = tracks['combined_info'].loc[playlist]
    playlist_df = playlist_df.reset_index()
    playlist_df.columns = ['Track_Id', 'Artist - Song Name - Genre']
    playlist_df.set_index('Track_Id', inplace=True)
    playlist_df.index.name = 'Track_Id'
    return playlist_df


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
        opacity=op,
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

    fig.update_layout(title='Deep Learning TSNE', autosize=True, width=1000, height=900, margin=dict(l=40, r=40, b=40, t=40))
    st.plotly_chart(fig)



def app():
    # Initialize session states

    if 'track1' not in st.session_state:
        st.session_state.track1 = None
    if 'track2' not in st.session_state:
        st.session_state.track2 = None
    if 'show_playlist' not in st.session_state:
        st.session_state.show_playlist = 'No'
    if 'length' not in st.session_state:
        st.session_state.length = 10

    c1, c2 = st.columns([5, 2])

    with c1:
        playlist = plot_dl_tsne(track_id_1=st.session_state.track1,
                track_id_2=st.session_state.track2,
                show_playlist=st.session_state.show_playlist,
                playlist_len=st.session_state.length)

    with c2:
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
        choose_playlist_length()
        st.radio('Show playlist', ('Yes', 'No'), key='show_playlist', index=1)

        playlist.style.hide_index()
        st.dataframe(playlist)
