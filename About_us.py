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
                    Web app<br>
                    
                    Data Analysis<br>

                    Visualization<br>
                    <br>
                    """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("Mariam Sudan ")
        st.markdown("23011154")
        st.markdown("""
                    Regular Expression<br>
                    
                    Data Analysis<br>

                    Report<br>
                    <br>
                    """, unsafe_allow_html=True)
    
    with col3:
        st.subheader("Mariam Osama")
        st.markdown("23012208")
        st.markdown("""
                    Visualization<br>
                    

                    Storage<br>
                    <br>
                    """, unsafe_allow_html=True)

    with col4:
        st.subheader("Menna Muhammed")
        st.markdown("23011565")
        st.markdown("""
                    Data Extraction<br>
                    
                    Data Cleaning<br>

                    Visualization<br>

                    Regression Model
                    """, unsafe_allow_html=True)
