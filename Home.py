import streamlit as st

def show():

    st.title("Welcome to Dettools 🧼")
    st.subheader("Here we kill errors with 99.9% accuracy ")

    with st.expander("What does this app provide ?"):
        st.write("""
                This is a simple data analysis app where you can
             
                -upload a dataset 
                 
                -view it in interactive table
                 
                -view charts and analysis
             
                Hope you enjoy our simple experiment 🤍
             """)
    

    