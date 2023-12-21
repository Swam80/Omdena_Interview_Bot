import streamlit as st

def User_info():
    st.title('Omdena Chat Bot for Interview')
    st.subheader('User Profile')
    name = st.text_input('Name')
    position = st.text_input('Position')


    experience_options = ['Select', 'Entry Level', 'Intermediate', 'Experienced']
    experience = st.selectbox('Experience', experience_options, index=0)


    
    job_link = st.text_input('Job Link')

    

    if st.button('Start Interview'):
        
        if name == '' or position == '' or experience == 'Select' or job_link == '':
            st.warning('Please fill out all fields.')
        else:
    
            st.write('Starting the interview...')
            return True
    return False

if __name__ == '__main__':
    User_info()
    