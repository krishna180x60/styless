from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_player import st_player
import webbrowser

#for emojis-> [ https://webfx.com/tools/emoji-cheat-sheet/ ]😼
st.set_page_config(page_title='gozo',page_icon="image/icon.png",layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css('style/style.css')