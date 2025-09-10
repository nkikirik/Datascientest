import streamlit as st
import pandas as pd

st.set_page_config(page_title="Leukovision", page_icon="🧫", layout="wide")

st.title("LeukoVision - White blood cell classification at a glance")
st.sidebar.title('Table of contents')

page = st.sidebar.radio("Go to", ["Home", "Introduction", "Preprocessing", "Modeling", "Evaluation" ])

intro = st.Page('./pages/Introduction.py', title = 'Introduction', icon = '📖')

pg = st.navigation([intro,
                    ], position='top')

pg.run()