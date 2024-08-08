import streamlit as st
from aster.db.sqlite3orm import SQLite3ORM

DB = "test.db"

if 'db' not in st.session_state:
    st.session_state.db = DB

st.set_page_config(
    page_title="Login Page",
    page_icon="🧊",
    # layout="wide",
    initial_sidebar_state="collapsed",
)

if "loginStatus" not in st.session_state:
    st.session_state.loginStatus = False

if st.session_state.loginStatus == False:
    st.switch_page("pages/login.py")

st.title("Welcome to the App")