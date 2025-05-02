import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import Dataset 
import plotly.express as px


def show():
    st.title("Plots ")

    if "file" not in st.session_state:
        st.warning("Please upload a dataset first.")
        return
    
    df = st.session_state["file"]


    #average price based on each column

    st.subheader("Average ")
    num_cols = df.select_dtypes(include=["int64", "float64"]).columns
    avg_y = st.selectbox("Select the feature you want to calculate its average", num_cols, key='avg_y')
    st.subheader("based on :")
    cols = df.columns 
    avg_x = st.selectbox("Select the feature you want to view the price based on", cols, key='avg_col')

    if avg_x == avg_y:
        st.warning(f"you cant view {avg_x} based on {avg_x} 🤨")
    else:
        avg_price_df = df.groupby(avg_x)[avg_y].mean().reset_index()
        st.write(avg_price_df)

    #plot it 

        fig = px.bar(avg_price_df, x=avg_x, y=avg_y, color=avg_x)
        st.plotly_chart(fig)





    # Pie Chart Section

    st.subheader("Pie Chart")

    cat_cols = df.select_dtypes(include=["object", "category"]).columns
    if len(cat_cols) == 0:
        st.info("No categorical columns available for pie chart ‼️")
        
    else:
        selected_col = st.selectbox("Select a categorical column:", cat_cols, key="pie_col")
        
        if len(df[selected_col].unique()) > 15:
            st.info("Too much values, not a proper visualization technique ‼️")
        else:
            value_counts = df[selected_col].value_counts()
            fig = px.pie(df, names=selected_col, title=f"Distribution of {selected_col}")
            st.plotly_chart(fig)




    # Scatter Plot Section
    st.subheader("📉 Scatter Plot")

    if len(num_cols) < 2:
        st.warning("Need at least two numeric columns to show a scatter plot.")
        return

    x = st.selectbox("Select X-axis column", num_cols, key="scatter_x")
    y = st.selectbox("Select Y-axis column", num_cols, key="scatter_y")

    fig, ax = plt.subplots()
    ax.scatter(df[x], df[y], alpha=0.6, color="teal")
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_title(f"{x} vs {y}")
    st.pyplot(fig)
    



    
    # Histograms for Numeric Columns
    st.subheader("📈 Histograms of Numeric Columns")

    num_cols = df.select_dtypes(include=["int64", "float64"]).columns

    if len(num_cols) == 0:
        st.info("No numeric columns to plot.")
        return

    selected_col = st.selectbox("Select a numeric column:", num_cols,key='hist_col')

    fig, ax = plt.subplots()
    ax.hist(df[selected_col], color="teal", edgecolor="black")
    ax.set_title(f"Histogram of {selected_col}")
    ax.set_xlabel(selected_col)
    ax.set_ylabel("Frequency")
    st.pyplot(fig)




    #heatmap
    
    st.subheader("Heatmap of Correlation Matrix")
    
    corr = df.corr(numeric_only=True)
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)



       
    
