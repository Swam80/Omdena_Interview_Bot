import random
import time
import streamlit as st
import speech_recognition as sr
import os

def User_info():
    st.sidebar.title('User Profile')
    
    name = st.sidebar.text_input('Name')
    
    position_options=['Select','Customer Service Representative', 'Sales Manager', 'Marketing Manager ','Nurse','Medical Assistance']
    position = st.sidebar.selectbox('Position', position_options, index=0)


    job_link = st.sidebar.text_input('Job Link')

    if not 'start_chat' in st.session_state:
        st.session_state.start_chat = False

    if st.sidebar.button('Start Interview',key="StartInterview"):
        if name == '' or position == 'Select'  or job_link == '':
            st.sidebar.warning('Please fill out all fields.')
            st.session_state.start_chat = False
        else:
            st.sidebar.write('Kindly answer on the chat input to the right ->')
            st.session_state.start_chat = True

    return st.session_state.start_chat