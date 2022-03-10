import streamlit as st


def vis():

    st.markdown("<h1 style='text-align: center; color: black;'>The Sonic Landscape through Tensorflow Projector</h1>", unsafe_allow_html=True)

    # Projector Tensorflow

    visualisation_ml = "https://projector.tensorflow.org/?config=https://gist.githubusercontent.com/scutellaria/6b7665ede566f36088a87b33da2ba620/raw/8d0c5d752a6ceda80da66c12ad0b8589af0eff25/ml_config.json"
    # st.write(f"Visualisation of features obtained from Machine Learning models [link]({visualisation_ml})")
    st.write(" ")
    st.write(" ")
    st.subheader(f"Visualisation of features obtained from Machine Learning models [link]({visualisation_ml})")


    visualisation_dl = "https://projector.tensorflow.org/?config=https://gist.githubusercontent.com/scutellaria/10af190769620674257419f80d5b50d7/raw/25027fd687c3bc0ac4285c3745cea592cca8eb06/config.json"
    #st.write(f"Visualisation of features obtained from Deep Learning models [link]({visualisation_dl})")
    st.subheader(f"Visualisation of features obtained from Deep Learning models [link]({visualisation_dl})")


def app():
    vis()
