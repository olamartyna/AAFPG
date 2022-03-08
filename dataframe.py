# loading dataframe - features reduced to about 200
# currently downloaded from local hard drive

import pandas as pd
import numpy as np
import streamlit as st

def loading_dataframe():
    st.write('This is our dataframe - metadata and reduced features')
    metadata_with_vectors_reduced = pd.read_csv('../AAFPG/data/metadata_with_vectors_reduced.csv')
    st.write(metadata_with_vectors_reduced.head(20))

def app():
    loading_dataframe()
