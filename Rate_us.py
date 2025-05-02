import streamlit as st

def show():

    
    col1, col2, col3 = st.columns([1, 2, 1]) 
    with col2:
        st.markdown(
        """
        <style>
        div.stButton > button {
            font-size: 20px;
            padding: 15px 40px;
            border-radius: 10px;
            background-color: #4CAF50;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
        st.title('How much do you like our app?')
        if st.feedback(options='faces'):
            st.balloons()
            st.balloons()

