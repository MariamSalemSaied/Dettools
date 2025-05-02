import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

def show():

    st.title("Who made this project")
    # Create 4 columns
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader("Mariam Salem ")
        st.markdown("23011151")
        st.markdown("""
                    Web app
                    
                    Data Analysis

                    Visualization
                    """)
    
    with col2:
        st.subheader("Mariam Sudan ")
        st.markdown("23011154")
        st.markdown("""
                    Regular Expression
                    
                    Data Analysis

                    Report
                    """)
    
    with col3:
        st.subheader("Mariam Osama")
        st.markdown("23012208")
        st.markdown("""
                    Visualization
                    

                    Storage
                    """)

    with col4:
        st.subheader("Menna Muhammed")
        st.markdown("23011565")
        st.markdown("""
                    Data Extraction
                    
                    Data Cleaning

                    Visualization

                    Regression Model
                    """)
