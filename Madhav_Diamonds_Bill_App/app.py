import streamlit as st
import pandas as pd
import subprocess, sys, tempfile, os
from models.billscrap import htmlcode

@st.cache_resource(show_spinner="Setting up PDF engine (first run only)...")
def install_chromium():
    subprocess.run(
        [sys.executable, "-m", "playwright", "install", "chromium"],
        check=True,
    )

install_chromium()

@st.cache_data(show_spinner="Creating PDF...")
def html_to_pdf(html: str) -> bytes:
    with tempfile.TemporaryDirectory() as tmp:
        html_path = os.path.join(tmp, "invoice.html")
        pdf_path = os.path.join(tmp, "invoice.pdf")

        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html)

        script = f'''
from playwright.sync_api import sync_playwright
import pathlib
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(pathlib.Path(r"{html_path}").as_uri(), wait_until="networkidle")
    page.pdf(path=r"{pdf_path}", format="A4", print_background=True,
             margin={{"top": "0", "right": "0", "bottom": "0", "left": "0"}})
    browser.close()
'''
        result = subprocess.run(
            [sys.executable, "-c", script],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            raise RuntimeError(result.stderr[-1500:])

        with open(pdf_path, "rb") as f:
            return f.read()

#our start from here

st.title("Madhav Diamonds", text_alignment="center")
st.header("Billing App", text_alignment="center")
st.write("A billing and business management application developed for Madhav Diamonds to streamline billing operations and improve the efficiency of daily business transactions. The application is designed to simplify invoice generation, manage customer billing details, and maintain organized transaction records through a user-friendly interface.")

st.divider()

Bno = st.number_input("Bill Number", min_value=1, max_value=10000, step=1)
Bdate = st.date_input(label="Invoice Date",format="DD/MM/YYYY")
Bname = st.text_input("Name of Invoice")

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

DJL = st.session_state.DJlist
QTYL = st.session_state.QTYlist
PL = st.session_state.Plist
TPL = st.session_state.TPlist

Hcode = htmlcode(Bdate, Bno, DJL, QTYL, PL, TPL, Gt, Bname)

pdf_bytes = html_to_pdf(Hcode)

st.download_button(
    label="Download Invoice PDF",
    data=pdf_bytes,
    file_name=f"Invoice_{Bno}.pdf",
    mime="application/pdf",
)

st.divider()

st.caption("Made with Love")
st.caption("Developed by: Rudram Devani")
