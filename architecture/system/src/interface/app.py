import streamlit as st

st.set_page_config(
    page_title="MedStudio - Comprehensive Intelligent Medical Platform", layout="wide"
)

import warnings

warnings.filterwarnings("ignore")

import sys
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="architecture/.env")

project_root = os.getenv("PROJECT_ROOT")

if project_root not in sys.path:
    sys.path.insert(0, project_root)



from architecture.system.src.interface.components import (
    chat_with_image,
    home,
    query,
    message,
    translate,
    drug_discovery,
    medical_search,
    message_base,
)

# from architecture.system.src.interface.components import medical_vqa


st.sidebar.title("📬🧬 MedStudio")
page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Home",
        "💬 Message",
        "💬 Basic message",
        "🔍 Medical retrieval",
        "🌐 Medical translate",
        "💬 Message with image",
        "🎰 Medical VQA",
        "💊 Drug discovery",
        "🩺 Medical search",
    ],
)


def load_styles(styles_path):
    with open(styles_path) as styles:
        st.markdown(f"<style>{styles.read()}</style>", unsafe_allow_html=True)


load_styles("architecture/system/src/interface/app.styles.css")

if page == "🏠 Home":
    home.render()
elif page == "💬 Message":
    message.render()
elif page == "💬 Basic message":
    message_base.render()
elif page == "🔍 Medical retrieval":
    query.render()
elif page == "🌐 Medical translate":
    translate.render()
elif page == "💬 Message with image":
    chat_with_image.render()
# elif page == "🎰 Medical VQA":
#     medical_vqa.render()
elif page == "💊 Drug discovery":
    drug_discovery.render()
elif page == "🩺 Medical search":
    medical_search.render()
