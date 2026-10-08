import streamlit as st
import pandas as pd

st.title("Madhav Diamonds")
st.header("Billing App")
st.write("Welcome to Madhav Diamonds Billing App, this app will help you to create the bills and manage the data")

st.divider()

tabdata = {}

DJdata = st.selectbox("Choose the Job Description", ["Select Option","DIAMOND JOB"])
QTYdata = st.text_input("Enter the Quantity")
Pdata = st.text_input("Enter the Unit Price")
n1 = float(QTYdata)
n2 = int(Pdata)
TPdata = n1*n2

DJlist = []
QTYlist = []
Plist = []
TPlist = []

if st.button("Add data"):
    DJlist.append(DJdata)
    QTYlist.append(QTYdata)
    Plist.append(Pdata)
    TPlist.append(TPdata)
    tabdata["Description"] = DJlist
    tabdata["Qty"] = QTYlist
    tabdata["Unit Price"] = Plist
    tabdata["Total Price"] = TPlist

df = pd.DataFrame(tabdata)
st.dataframe(df)