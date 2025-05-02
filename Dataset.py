import streamlit as st
import numpy as np
import pandas as pd

def show():

    st.title("Dataset")

    if "file" in st.session_state:
        st.write("Using previously uploaded data:")
        st.dataframe(st.session_state["file"])
        return  

    file = st.file_uploader('Upload your dataset', type=["csv"], accept_multiple_files=False)

    if file is not None:
        df = pd.read_csv(file)
        st.session_state["file"] = df  
        st.success("File uploaded successfully!")
        st.dataframe(df)
        

    


    
