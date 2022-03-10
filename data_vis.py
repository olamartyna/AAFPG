# import pandas as pd
# import numpy as np
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.decomposition import PCA
# import plotly.graph_objects as go
# import plotly.express as px
import streamlit as st
# import streamlit.components.v1 as components
# import plotly.graph_objects as go


def vis():

    st.header('The Sonic Landscape through Tensorflow Projector')
    st.markdown("<h1 style='text-align: center; color: red;'>Some title</h1>", unsafe_allow_html=True)

    # Projector Tensorflow

    visualisation_ml = "https://projector.tensorflow.org/?config=https://gist.githubusercontent.com/scutellaria/6b7665ede566f36088a87b33da2ba620/raw/8d0c5d752a6ceda80da66c12ad0b8589af0eff25/ml_config.json"
    st.write(f"Visualisation of features obtained from Machine Learning models [link]({visualisation_ml})")
    # components.iframe(visualisation_ml, scrolling=False, width=1200, height=800)


    visualisation_dl = "https://projector.tensorflow.org/?config=https://gist.githubusercontent.com/scutellaria/10af190769620674257419f80d5b50d7/raw/25027fd687c3bc0ac4285c3745cea592cca8eb06/config.json"
    st.write(f"Visualisation of features obtained from Deep Learning models [link]({visualisation_dl})")
    # components.iframe(visualisation_dl, scrolling=False, width=1200, height=800)

# def header(url):
#      st.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:24px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)


def app():
    vis()
