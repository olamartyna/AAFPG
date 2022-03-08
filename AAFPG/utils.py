# functions for calling and manipulating data, connecting metadata with files

import pandas as pd
import librosa
import matplotlib.pyplot as plt
import numpy as np
import librosa.display
import os
from IPython.display import Audio
import random
from sklearn.model_selection import train_test_split
import tensorflow as tf
import tensorflow_io as tfio
from tqdm.auto import tqdm
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint



def get_features(path='/content/drive/MyDrive/AAFPG/fma_metadata/features.csv'):

    '''imports the features.csv dataset as a pandas dataframe'''

    features = pd.read_csv(path, index_col=0, header=[0, 1, 2])
    return features

def get_tracks(path='/content/drive/MyDrive/AAFPG/fma_metadata/tracks.csv'):

    '''imports the tracks.csv dataset as a pandas dataframe'''

    tracks = pd.read_csv(path, index_col=0, header=[0, 1])
    return tracks

def get_tracks_paths_from_dir(top_dir):

    '''returns track a list of all track ids and paths within a specified
    directory, including sub-dirs, as a tuple'''

    tracks_ids = []
    track_paths = {}
    for root, dirs, files in os.walk(top_dir, topdown=True):
        for file in files:
            if '.mp3' in file:
                track_id = int(file.replace('.mp3',''))
                track_paths[track_id]= (os.path.join(root, file))
                tracks_ids.append(track_id)
    return tracks_ids, track_paths


def get_features_subset(path_to_track_dir,
                        path_featurs_csv='/content/drive/MyDrive/AAFPG/fma_metadata/features.csv'):

    '''imports the features.csv dataset as a pandas dataframe,
    reduces it to the tracks found within the specified directory'''

    tracks_ids, tracks_paths = get_tracks_paths_from_dir(top_dir=path_to_track_dir)
    features = get_features(path=path_featurs_csv)
    features_subset = features.loc[sorted(tracks_ids)]
    return features_subset

def get_tracks_subset(path_to_track_dir,
                      path_tracks_csv='/content/drive/MyDrive/AAFPG/fma_metadata/tracks.csv'):

    '''imports the tracks.csv dataset as a pandas dataframe,
     reduces it to the tracks found within the specified directory'''

    tracks_ids, tracks_paths = get_tracks_paths_from_dir(top_dir=path_to_track_dir)

    tracks = get_tracks(path=path_tracks_csv)
    tracks_subset = tracks.loc[sorted(tracks_ids)]
    return tracks_subset

def get_genres(path='/content/drive/MyDrive/AAFPG/fma_metadata/genres.csv'):

    '''imports the tracks.csv dataset as a pandas dataframe'''

    genres = pd.read_csv(path, index_col=0)
    return genres

def get_tracks_genres_subset(path_to_track_dir,
                             path_genres_csv='/content/drive/MyDrive/AAFPG/fma_metadata/genres.csv',
                             path_tracks_csv='/content/drive/MyDrive/AAFPG/fma_metadata/tracks.csv'):

    '''builds as tracks_genres dataframe including filepaths for tracks within
    a given directory, including sub-directories'''

    tracks_ids, tracks_paths = get_tracks_paths_from_dir(top_dir=path_to_track_dir)
    tracks = get_tracks_subset(path_to_track_dir=path_to_track_dir,
                               path_tracks_csv=path_tracks_csv)
    genres = get_genres(path=path_genres_csv)
    tracks_subset = tracks.loc[sorted(tracks_ids)]
    tracks_genres_subset = tracks_subset[[('track','genre_top'),('track','genres'),('track','genres_all')]].copy()
    tracks_genres_subset['path'] = tracks_genres_subset.index.map(tracks_paths)
    tracks_genres_subset['path_relative'] = tracks_genres_subset['path'].apply(lambda x: x.replace(path_to_track_dir,''))
    tracks_genres_subset.columns = ['genre_top','genres','genres_all','path','path_relative']
    tracks_genres_subset['genres'] = tracks_genres_subset['genres'].apply(lambda x: genre_id_to_string(x))
    tracks_genres_subset['genres_all'] = tracks_genres_subset['genres_all'].apply(lambda x: genre_id_to_string(x))
    return tracks_genres_subset

def get_genre_top_dict_subset(path_to_track_dir,
                             path_genres_csv='/content/drive/MyDrive/AAFPG/fma_metadata/genres.csv',
                             path_tracks_csv='/content/drive/MyDrive/AAFPG/fma_metadata/tracks.csv'):

    '''builds a dictionary with genres_top as keys, lists of tracks in a given
    directory as values'''

    genre_top_dict_subset = {}
    tracks_genres_subset = get_tracks_genres_subset(path_to_track_dir=path_to_track_dir,
                                                        path_genres_csv=path_genres_csv,
                                                        path_tracks_csv=path_tracks_csv)

    for genre in tracks_genres_subset['genre_top'].unique():
        genre_top_dict_subset[genre] = []
    for track in tracks_genres_subset.index:
        genre_top_dict_subset[tracks_genres_subset.loc[track][0]].append(track)
    return genre_top_dict_subset

def genre_id_to_string(string, path_genres_csv='/content/drive/MyDrive/AAFPG/fma_metadata/genres.csv'):

    '''converts genre ids from the genres cells of the tracks df to gernes'''
    genres = get_genres(path=path_genres_csv)
    string = string.replace('[','').replace(']','').replace(',','')
    if ' ' in string:
        string_list = string.split(' ')
    else:
        string_list = []
        string_list.append(string)
    int_list = []
    for string in string_list:
        int_list.append(int(string))

    genre_list = []
    for genre_id in int_list:
        genre_list.append(genres.loc[genre_id][2])

    return ', '.join(genre_list)

def play_track(track_id_or_list, path_to_fma_small='/content/drive/MyDrive/AAFPG/fma_small'):

    tracks = get_tracks()
    disp_info = tracks[[('artist', 'name'),('track','title'),('track','genre_top')]]
    path_dict = get_tracks_paths_from_dir(path_to_fma_small)[1]


    if type(track_id_or_list) == int:
        track_id = track_id_or_list
        track_info = disp_info.loc[track_id]
        print(f'Artist: {track_info[0]}, Track: {track_info[1]}, Genre: {track_info[2]}')
        IPython.display.display(Audio(path_dict[track_id]))
        print('\n')
    if type(track_id_or_list) == list:
        track_list = track_id_or_list
        for track_id in track_list:
            track_info = disp_info.loc[track_id]
            print(f'Artist: {track_info[0]}, Track: {track_info[1]}, Genre: {track_info[2]}')
            IPython.display.display(Audio(path_dict[track_id]))
            print('\n')
