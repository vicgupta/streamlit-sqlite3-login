import streamlit as st
import time
from aster.db.sqlite3orm import SQLite3ORM

if 'db' not in st.session_state:
    st.switch_page("app.py")
else:
    db = SQLite3ORM(st.session_state.db)

st.set_page_config(
    page_title="Text to Speech (by Bing)",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.title("Login Page")

login_tab, signup_tab = st.tabs(["Login", "Signup"])

with signup_tab:
    st.title('Signup')
    with st.form(key='signup_form'):
        email = st.text_input('Email', max_chars=200)
        password = st.text_input('Password', type='password', help='Need minimum 8 characters')
        password2 = st.text_input('Confirm Password', type='password')
        submit_button = st.form_submit_button(label='Signup')
        if password != password2:
            st.write('Passwords do not match. Please try again.')
            st.stop()
        if submit_button:
            response = db.signup('users', email, password)
            if response:
                st.write(response)
                st.session_state.loginStatus = True
                st.session_state.email = email
                st.write('Signup successful!')
                st.switch_page("app.py")
            else:
                st.write('Signup failed. Please try again.')
                st.spinner()
                time.sleep(5)
            st.rerun()

with login_tab:
    st.title('Login')
    with st.form(key='login_form'):
        email = st.text_input('Email')
        password = st.text_input('Password', type='password')
        submit_button = st.form_submit_button(label='Login')
        if submit_button:
            if db.login('users', email, password):
                st.write('Login successful!')
                st.session_state.loginStatus = True
                st.session_state.email = email
                st.switch_page("app.py")
            else:
                st.write('Login failed. Please try again.')
                st.spinner()
                time.sleep(5)
                st.rerun()

