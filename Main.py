import streamlit as st
from Recommend import df, recommend

# Set custom Streamlit page config
st.set_page_config(
    page_title="Music Recommender 🎵",
    page_icon="🎧",  # You can also use a path to a .ico or .png file
    layout="centered"
)

col1, col2 = st.columns(2)
with col1:
    st.image('newlogo.jpeg')
with col2:
    st.title("Music Recommender Engine")

st.markdown('---')
col1, col2 = st.columns(2)
with col1:
    st.image('format.jpeg',width=350)
with col2:
    st.subheader('Have the ability to control your Classic music')
st.markdown('---')
song_list = sorted(df['song'].dropna().unique())
selected_song = st.selectbox("🎵 Select a song:", song_list)

if st.button("🚀 Recommend Similar Songs"):
    with st.spinner("Finding similar songs..."):
        recommendations = recommend(selected_song)
        if recommendations is None:
            st.warning("Sorry, song not found.This is only based on the dataset")
        else:
            st.success("This is what you may like:")
            st.table(recommendations)