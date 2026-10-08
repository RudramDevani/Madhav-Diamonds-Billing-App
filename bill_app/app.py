import streamlit as st

st.title("Madhav Diamonds")
st.header("Billing App")
st.write("Welcome to Madhav Diamonds Billing App, this app will help you to create the bills and manage the data")

st.divider()

tabdata = {}

DJdata = st.selectbox("Choose the Job Description", ["DIAMOND JOB"])