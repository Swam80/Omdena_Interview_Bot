import random
import time
import streamlit as st

def User_info():
    st.sidebar.title('User Profile')
    
    name = st.sidebar.text_input('Name')
    
    position_options=['Select','Customer Service Representative', 'Sales Manager', 'Marketing Manager ','Nurse','Medical Assistance']
    position = st.sidebar.selectbox('Position', position_options, index=0)

    experience_options = ['Select', 'Entry Level', 'Intermediate', 'Experienced']
    experience = st.sidebar.selectbox('Experience', experience_options, index=0)

    job_link = st.sidebar.text_input('Job Link')

    if not 'start_chat' in st.session_state:
        st.session_state.start_chat = False

    if st.sidebar.button('Start Interview'):
        if name == '' or position == '' or experience == 'Select' or job_link == '':
            st.sidebar.warning('Please fill out all fields.')
            st.session_state.start_chat = False
        else:
            st.sidebar.write('Kindly answer on the chat input to the right ->')
            st.session_state.start_chat = True

    return st.session_state.start_chat


def display_chat(start_chat):
    st.title("Omdena Interview Bot")

    # Initialize chat history with a welcome message
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role" : "assistant" , "content":"Hi, I will be proceeding with your interview today. All the Best! Shall we start?"}]

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Sample Questions
    questions = ["Great! Tell me about your educational background","Briefly elaborate on your working experience","How does you experience align with the Job Profile"]

    # Accept user input
    if start_chat:
        if prompt := st.chat_input("ANSWER"):
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(prompt)

            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                
                assistant_response = questions[len(st.session_state.messages)//2-1] #This was done to increment the question index

                # Simulate stream of response with milliseconds delay
                for chunk in assistant_response.split():
                    full_response += chunk + " "
                    time.sleep(0.05)
                    # Add a blinking cursor to simulate typing
                    message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": full_response})

start_chat = User_info()
display_chat(start_chat)


