import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

def show():
    st.title("Descriptive Analysis")

    if "file" not in st.session_state:
        st.warning("Please upload a dataset first.")
        return

    df = st.session_state["file"]

    # Dataset Overview
    

    st.subheader("Dataset Overview")
    st.write(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")

    st.write("**Column Data Types:**")
    st.write(df.dtypes)


    # Descriptive Stats

    st.subheader("Descriptive Statistics")
    st.write(df.describe())


    # Value Counts for Categoricals

    st.subheader("Categorical Column Summary")
    cat_cols = df.select_dtypes(include=["object", "category"]).columns

    if len(cat_cols) > 0:
        col = st.selectbox("Select a categorical column:", cat_cols)
        st.write(df[col].value_counts())
    else:
        st.info("No categorical columns found.")


   