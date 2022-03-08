# Visualisation: PCA and Tensorflow Projector
# Using dataframe with features reduced to about 200 - downloaded from local drive

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objects as go

# PCA
# 3D plotly scatter plot from Keith's merged df

@st.cache
def get_plotly_data():

    z_data = pd.read_csv("../AAFPG/data/metadata_with_vectors_reduced.csv")
    z = z_data.values
    sh_0, sh_1 = z.shape
    x, y = np.linspace(0, 1, sh_0), np.linspace(0, 1, sh_1)
    return x, y, z


def vis():
    # Extract input data (X)
    metadata_with_vectors_reduced= pd.read_csv("../AAFPG/data/metadata_with_vectors_reduced.csv")
    X = metadata_with_vectors_reduced.drop([
    'track_id',
    'artist_name',
    'album_title',
    'track_title',
    'track_genre_top',
    'track_genres',
    'track_genres_all',
    'track_genres_string',
    'track_genres_all_string',
    'path_relative'],
    axis=1)

    X_features = X.columns

    y = metadata_with_vectors_reduced['track_genre_top']

    # Data must be centered around their mean before applying PCA
    scaler = MinMaxScaler()
    scaler.fit(X)
    X = pd.DataFrame(scaler.transform(X), columns=X_features)

    # let's create a PCA with 3 components for visulaisation
    pca_3 = PCA(n_components=3)
    pca_3.fit(X)

    #project our data
    X_proj_3 = pca_3.transform(X)
    X_proj_3 = pd.DataFrame(X_proj_3, columns=[f'PC{i}' for i in range(1, 4)])

    # create a df with the new PCs and the categories and labels
    plot_data_pca = X_proj_3.join(y)
    #plot_data_pca = plot_data_pca.join(track_labels)
    plot_list_pca = (list(range(0,len(metadata_with_vectors_reduced), 3)))
    plot_data_reduced_pca = plot_data_pca.iloc[plot_list_pca]

    # Create 3-D plot using plotly
    # colours are genres
    # data-points labeled with artist_name-track_name

    fig = px.scatter_3d(plot_data_reduced_pca, x='PC1', y='PC2', z='PC3', opacity=0.5, color='track_genre_top')

    # tight layout
    fig.update_traces(marker_size = 4)
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))


    x, y, z = get_plotly_data()

    # fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
    fig.update_layout(title='PCA', autosize=False, width=800, height=800, margin=dict(l=40, r=40, b=40, t=40))
    st.plotly_chart(fig)



    # Projector Tensorflow

    # visualisation = "https://projector.tensorflow.org/?config=https://gist.githubusercontent.com/scutellaria/6dd9a7008fe925a2d4ddaf8498ea79cb/raw/800b440e0503241619490f4189ce2b84e62a97ab/config.json"
    visualisation = "https://gist.githubusercontent.com/scutellaria/6dd9a7008fe925a2d4ddaf8498ea79cb/raw/800b440e0503241619490f4189ce2b84e62a97ab/config.json"
    st.write(f"check out this [link]({visualisation})")

    components.iframe("https://projector.tensorflow.org/", scrolling=False, width=1200, height=800)


def app():
    vis()
