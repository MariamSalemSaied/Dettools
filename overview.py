import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
import streamlit as st
from streamlit_pandas_profiling import st_profile_report


def show():

    st.title("Dataset Overview")

    if "file" not in st.session_state:
        st.warning("Please upload a dataset first.")
        return

    df = st.session_state["file"]
    pr = df.profile_report()
    st_profile_report(pr)
    