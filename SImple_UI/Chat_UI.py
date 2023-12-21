import random
import time
import streamlit as st

def display_chat():
    st.title("Omdena Interview Bot")

    # Initialize chat history wiht a welcome message
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role" : "assistant" , "content":"Hi, I will be proceeding with your interview today. All the Best! Shall we start?"}]

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Sample Questions
    questions = ["Great! Tell me about your educational background","Briefly elaborate on your working experience","How does you experience align with the Job Profile"
    ]

    # Accept user input

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


if __name__ == '__main__':
    display_chat()

