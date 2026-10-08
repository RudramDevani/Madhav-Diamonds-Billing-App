import streamlit as st
import pandas as pd

st.title("Madhav Diamonds")
st.header("Billing App")
st.write("Welcome to Madhav Diamonds Billing App, this app will help you to create the bills and manage the data")

DJlist = []
QTYlist = []
Plist = []
TPlist = []

st.divider()

tabdata = {}

length = st.number_input("enter how many data need to add", min_value=1, max_value=9, step=1)
for i in range(0, length):
    DJdata = st.selectbox("Choose the Job Description", ["Select Option","DIAMOND JOB"])
    QTYdata = st.number_input("Enter the Quantity",min_value=0.01, max_value=100000.00, step=0.01)
    Pdata = st.number_input("Enter the Unit Price", min_value=0.01, max_value=10000.00, step=0.01)
    TPdata = QTYdata*Pdata
    QTYlist.append(QTYdata)


st.write(QTYlist)