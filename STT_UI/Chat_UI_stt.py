
import time
import streamlit as st
import speech_recognition as sr
import os
from UserInfo import User_info

start_chat = User_info()

def display_chat(start_chat):

    st.title("Omdena Interview Bot")

    # Initialize recording state
    if "recording" not in st.session_state:
        st.session_state.recording = False
    
    # To replace the button instructions in the same place we use placeholder. So that new element is not created for every click.
    placeholder = st.empty()

    if st.button("Start Recording",key="RecordStart"):
        st.session_state.recording = True
        placeholder.text('Wait for a few seconds!\n The recording will stop automatically after a period of silence.')

    if start_chat:

        # Initialize chat history with a welcome message
        if "messages" not in st.session_state:
            st.session_state.messages = [{"role" : "assistant" , "content":"Hi, I will be proceeding with your interview today. All the Best! Shall we start?"}]

        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Sample Questions
        questions = ["Great! Tell me about your educational background","Briefly elaborate on your working experience","How does you experience align with the Job Profile"]

        # Accept user input using STT
        transcription = ""
            
        if st.session_state.recording:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                placeholder.text("Start with your answer")
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    transcription += text + " "
                except sr.UnknownValueError:
                    st.write("Could not understand audio")
                except sr.RequestError as e:
                    st.error(f"Could not request results from speech recognition service; {e}")

        # Save the transcribed text
        if transcription:
            placeholder.text("Thank you for the answer")
            time.sleep(2)
            placeholder.empty()

            with open(os.path.join(os.getcwd(),'transcription.txt'), 'a') as f:
                f.write(transcription + '\n')

            st.session_state.messages.append({"role": "user", "content": transcription})

            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                assistant_response = questions[len(st.session_state.messages)//2-1] #This was done to increment the question index
                st.markdown(assistant_response)

                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})

# Run the display function
display_chat(start_chat)
