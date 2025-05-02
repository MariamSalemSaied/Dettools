# libraries
import streamlit as st
import Home
import Dataset
import overview 
import Descriptive
import Charts 
import Our_Analysis
import Our_linreg_model
import About_us
import Rate_us

#background color
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(45deg, #169976, #73C7C7, #FFC785, #FF9EAA, #D291BC);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }

    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    </style>
    """,
    unsafe_allow_html=True
    )
st.sidebar.markdown("<h1 style='font-size: 48px;'>🔬</h1>", unsafe_allow_html=True)

#side bar 
# image
background_url = "https://i.postimg.cc/R099PNHr/Colorful-Cute-Kids-Stationary-Page-Border-2.png"  
st.markdown(f"""
    <style>
    [data-testid="stSidebar"] {{
        position: relative;
        overflow: hidden;
        background-image: url("{background_url}");
        background-size: cover;
        background-position: center;
        color: #111111 !important;  /* Force dark text */
    }}

    /* Override text inside sidebar */
    [data-testid="stSidebar"] * {{
        color: #111111 !important;
        font-weight: 600;
    }}
    </style>
""", unsafe_allow_html=True)
# content
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Dataset", "Dataset Overview", "Descriptive Analysis", "Charts", "Our Analysis", "Our Linear Regression Model", "About us", "Rate us"])


#traversing through pages 
if page == "Home":
    Home.show()
elif page == "Charts":
    Charts.show()
elif page == "Dataset":
    Dataset.show()
elif page== "Dataset Overview":
    overview.show()
elif page == "Descriptive Analysis":
    Descriptive.show()
elif page == "Our Analysis":
    Our_Analysis.show()
elif page == "Our Linear Regression Model":
    Our_linreg_model.show()
elif page == "About us":
    About_us.show()
elif page == "Rate us":
    Rate_us.show()
 
