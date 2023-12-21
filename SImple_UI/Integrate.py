import UserProfile_streamlit 
from Chat_UI import display_chat 
import streamlit as st

def app1():
    button_pressed = UserProfile_streamlit.User_info() 
    if button_pressed:
        st.session_state.app = app2
        st.experimental_rerun()

def app2():
    display_chat()

if 'app' not in st.session_state:
    st.session_state.app = app1

st.session_state.app()
