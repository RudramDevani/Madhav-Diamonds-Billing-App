import streamlit as st
import pandas as pd

st.title("Madhav Diamonds", text_alignment="center")
st.header("Billing App", text_alignment="center")
st.write("Welcome to Madhav Diamonds Billing App, this app will help you to create the bills and manage the data")

st.divider()

tabdata = {}

if "SRlist" not in st.session_state:
    st.session_state.SRlist = []
if "SR" not in st.session_state:
    st.session_state.SR = 1
if "DJlist" not in st.session_state:
    st.session_state.DJlist = []
if "QTYlist" not in st.session_state:
    st.session_state.QTYlist = []
if "Plist" not in st.session_state:
    st.session_state.Plist = []
if "TPlist" not in st.session_state:
    st.session_state.TPlist = []

DJdata = st.selectbox("Select the Work Description", ['DIAMOND JOB'])
QTYdata = st.number_input("Enter the Quantity", min_value=0.01, max_value=10000.00, step=0.01)
Pdata = st.number_input("Enter the Unit Price", min_value=0.01, max_value=10000.00, step=0.01 )
TPdata = QTYdata * Pdata

if st.button("Add Data"):
    st.session_state.DJlist.append(DJdata)
    st.session_state.QTYlist.append(QTYdata)
    st.session_state.Plist.append(Pdata)
    st.session_state.TPlist.append(TPdata)
    st.session_state.SRlist.append(st.session_state.SR)
    st.session_state.SR += 1

tabdata["Sr. No."] = st.session_state.SRlist
tabdata["Description"] = st.session_state.DJlist
tabdata["Qty"] = st.session_state.QTYlist
tabdata["Unit Price"] = st.session_state.Plist
tabdata["Total Price"] = st.session_state.TPlist

df = pd.DataFrame(tabdata)
st.dataframe(df, hide_index=True)

Gt = sum(st.session_state.TPlist)
st.write("Grand Total: ", Gt)
