import streamlit as st
import pandas as pd

st.title("Madhav Diamonds", text_alignment="center")
st.header("Billing App", text_alignment="center")
st.write("A billing and business management application developed for Madhav Diamonds to streamline billing operations and improve the efficiency of daily business transactions. The application is designed to simplify invoice generation, manage customer billing details, and maintain organized transaction records through a user-friendly interface.")

st.divider()

Bno = st.number_input("Enter the Bill Number", min_value=1, max_value=10000, step=1)
c1, c2, c3 = st.columns(3)
with c1:
    day = st.number_input("Enter the day", min_value=1, max_value=31, step=1)

with c2:
    month = st.number_input("Enter the month", min_value=1, max_value=12, step=1)

with c3:
    year = st.number_input("Enter the year", min_value=2000, max_value=3000, step=1)

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

col0, col1, col2 = st.columns(3)

with col0:

    if st.button("Add Data"):
        st.session_state.DJlist.append(DJdata)
        st.session_state.QTYlist.append(QTYdata)
        st.session_state.Plist.append(Pdata)
        st.session_state.TPlist.append(TPdata)
        st.session_state.SRlist.append(st.session_state.SR)
        st.session_state.SR += 1

with col1:
    sno = st.number_input("Enter Sr. No. you want to delete", min_value = 1, max_value = 9, step=1)
    ind = sno - 1
    if st.button("Delete the Row"):
        st.session_state.SRlist.pop()
        st.session_state.DJlist.pop()
        st.session_state.QTYlist.pop(ind)
        st.session_state.Plist.pop(ind)
        st.session_state.TPlist.pop(ind)
        st.session_state.SR -= 1

with col2:
    if st.button("Delete All"):
        st.session_state.SRlist.clear()
        st.session_state.DJlist.clear()
        st.session_state.QTYlist.clear()
        st.session_state.Plist.clear()
        st.session_state.TPlist.clear()
        st.session_state.SR = 1

tabdata["Sr. No."] = st.session_state.SRlist
tabdata["Description"] = st.session_state.DJlist
tabdata["Qty"] = st.session_state.QTYlist
tabdata["Unit Price"] = st.session_state.Plist
tabdata["Total Price"] = st.session_state.TPlist

df = pd.DataFrame(tabdata)
st.dataframe(df, hide_index=True)

Gt = sum(st.session_state.TPlist)
st.write("Grand Total: ", Gt)

st.divider()

