import streamlit as st
import pandas as pd

st.title("Madhav Diamonds")
st.header("Billing App")
st.write("Welcome to Madhav Diamonds Billing App, this app will help you to create the bills and manage the data")

st.divider()

tabdata = {}

DJlist = []
Qtylist = []
Plist = []
TPlist = []

opt = [1,2,3,4,5,6,7,8,9]
index = st.selectbox(label="Sr. No.", options=opt)

if index == 1:
    djd = st.selectbox("Work Description", ["Select the Description", "DIAMOND WORK"])
    qtyd = st.number_input("Enter Quantity", min_value=0.01, max_value=10000.00, step=0.01)
    pdata = st.number_input("Enter Unit Price", min_value=0.01, max_value=10000.00, step=0.01)
    tpd = qtyd * pdata
    if st.button("Add Data"):
        DJlist.append(djd)
        Qtylist.append(qtyd)
        Plist.append(pdata)
        TPlist.append(tpd)

if index == 2:
    djd = st.selectbox("Work Description", ["Select the Description", "DIAMOND WORK"])
    qtyd = st.number_input("Enter Quantity", min_value=0.01, max_value=10000.00, step=0.01)
    pdata = st.number_input("Enter Unit Price", min_value=0.01, max_value=10000.00, step=0.01)
    tpd = qtyd * pdata
    if st.button("Add Data"):
        DJlist.append(djd)
        Qtylist.append(qtyd)
        Plist.append(pdata)
        TPlist.append(tpd)

st.write(Qtylist)